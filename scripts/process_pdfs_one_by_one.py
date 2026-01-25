#!/usr/bin/env python3
"""
Process PDFs one at a time with real-time logging and careful image/graph handling.
Asks for feedback after each PDF before proceeding.
"""

import os
import sys
import pdfplumber
from pdf2image import convert_from_path
from pathlib import Path
import requests
import json
import re
from datetime import datetime
import time

# Global log file
LOG_FILE = None

def log(message, level="INFO"):
    """Write to both console and log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{level}] {message}"
    print(log_message)
    if LOG_FILE:
        LOG_FILE.write(log_message + "\n")
        LOG_FILE.flush()  # Ensure real-time writing

def get_poe_api_key():
    """Read Poe API key from LLM/poe.md"""
    poe_file = Path(__file__).parent / "LLM" / "poe.md"
    if poe_file.exists():
        with open(poe_file, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip() and not line.strip().startswith('http')]
            if lines:
                return lines[0]
    return None

def extract_images_from_pdf(pdf_path, output_dir):
    """Extract images and charts from PDF pages with careful handling."""
    images_info = []
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    log(f"Extracting images from: {pdf_path.name}")
    
    try:
        # Convert PDF pages to high-resolution images
        log(f"  Converting PDF pages to images (300 DPI)...")
        images = convert_from_path(pdf_path, dpi=300, fmt='png')
        log(f"  Converted {len(images)} pages to images")
        
        # Also try to extract embedded images/charts from PDF structure
        embedded_images = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                # Check for images in page
                if hasattr(page, 'images') and page.images:
                    log(f"  Found {len(page.images)} embedded image(s) on page {page_num}")
                    for img_idx, img in enumerate(page.images):
                        embedded_images.append({
                            'page': page_num,
                            'index': img_idx,
                            'bbox': (img.get('x0', 0), img.get('top', 0), img.get('x1', 0), img.get('bottom', 0)),
                            'width': img.get('width', 0),
                            'height': img.get('height', 0)
                        })
        
        # Save page images
        for page_num, img in enumerate(images, 1):
            img_filename = f"page_{page_num:03d}.png"
            img_path = output_dir / img_filename
            img.save(img_path, 'PNG', quality=95)
            images_info.append({
                'page': page_num,
                'path': str(img_path),
                'filename': img_filename,
                'type': 'full_page'
            })
            log(f"  Saved page {page_num} image: {img_filename} ({img.size[0]}x{img.size[1]})")
        
        if embedded_images:
            log(f"  Note: Found {len(embedded_images)} embedded image references (coordinates available)")
        
        return images_info
    except Exception as e:
        log(f"Error extracting images: {e}", "ERROR")
        import traceback
        log(traceback.format_exc(), "ERROR")
        return []

def extract_text_with_structure(pdf_path):
    """Extract text from PDF with structure preservation."""
    text_content = []
    log(f"Extracting text from: {pdf_path.name}")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            log(f"  PDF has {total_pages} pages")
            
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    text_content.append({
                        'page': page_num,
                        'text': text,
                        'char_count': len(text)
                    })
                    log(f"  Page {page_num}: Extracted {len(text)} characters")
                else:
                    log(f"  Page {page_num}: No text found (may be image-only page)", "WARNING")
                    text_content.append({
                        'page': page_num,
                        'text': f"[Image-only page - see page_{page_num:03d}.png]",
                        'char_count': 0
                    })
            
            total_chars = sum(p['char_count'] for p in text_content)
            log(f"  Total text extracted: {total_chars} characters from {len(text_content)} pages")
            
    except Exception as e:
        log(f"Error extracting text: {e}", "ERROR")
        import traceback
        log(traceback.format_exc(), "ERROR")
        return []
    
    return text_content

def call_poe_api(prompt, api_key, max_retries=2):
    """Call Poe API to process content with LLM."""
    if not api_key:
        log("No Poe API key found. Skipping LLM processing.", "WARNING")
        return None
    
    try:
        url = "https://api.poe.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "Claude-3.5-Sonnet",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 16000,
            "temperature": 0.3
        }
        
        log(f"  Calling Poe API (model: Claude-3.5-Sonnet)...")
        start_time = time.time()
        
        for attempt in range(max_retries):
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=180)
                
                if response.status_code == 200:
                    result = response.json()
                    content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
                    elapsed = time.time() - start_time
                    log(f"  ✓ API call successful ({elapsed:.1f}s, {len(content)} chars returned)")
                    return content
                else:
                    log(f"  API error (attempt {attempt+1}/{max_retries}): {response.status_code} - {response.text[:200]}", "WARNING")
                    if attempt < max_retries - 1:
                        time.sleep(2)  # Wait before retry
            except requests.Timeout:
                log(f"  API timeout (attempt {attempt+1}/{max_retries})", "WARNING")
                if attempt < max_retries - 1:
                    time.sleep(2)
        
        return None
    except Exception as e:
        log(f"Error calling Poe API: {e}", "ERROR")
        return None

def format_markdown_with_llm(text_content, images_info, api_key, session_num):
    """Use LLM to format markdown content properly."""
    log(f"Formatting markdown with LLM (Session {session_num})...")
    
    # Build complete raw markdown with all content
    full_raw_md = []
    full_raw_md.append(f"# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}\n")
    full_raw_md.append("---\n")
    
    for page_data in text_content:
        full_raw_md.append(f"\n## Page {page_data['page']}\n\n")
        full_raw_md.append(page_data['text'])
        full_raw_md.append("\n")
    
    raw_content = "\n".join(full_raw_md)
    log(f"  Prepared {len(raw_content)} characters of raw content")
    
    # Prepare image references
    image_refs = ""
    if images_info:
        image_refs = "\n---\n\n## Images and Charts\n\n"
        for img_info in images_info:
            session_folder = Path(img_info['path']).parent.name
            rel_path = f"images/{session_folder}/{img_info['filename']}"
            image_refs += f"### Page {img_info['page']}\n\n"
            image_refs += f"![Page {img_info['page']}]({rel_path})\n\n"
    
    # Process in chunks if content is too long
    if len(raw_content) > 12000:
        log(f"  Content too long ({len(raw_content)} chars), processing page by page...")
        formatted_parts = []
        formatted_parts.append(f"# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}\n")
        formatted_parts.append("---\n")
        
        for page_data in text_content:
            page_text = page_data['text']
            if len(page_text) < 50:  # Image-only page
                formatted_parts.append(f"\n## Page {page_data['page']}\n\n")
                formatted_parts.append(page_text)
                formatted_parts.append("\n")
            else:
                prompt = f"""Format this single page from a PDF into markdown. CRITICAL: Preserve ALL text exactly - do NOT summarize or omit anything.

Requirements:
- Keep "## Page {page_data['page']}" as the heading
- Format lists: "- " for bullets, "1. " for numbered
- Make task titles bold: **Task X**
- Format URLs: [text](url)
- Preserve ALL content - every word must be included
- Do NOT add "[Continues...]" or summaries

Page Content:
{page_text}

Return ONLY the formatted markdown for this page, starting with "## Page {page_data['page']}":"""
                
                formatted_page = call_poe_api(prompt, api_key)
                if formatted_page:
                    # Remove any "I'll help" or similar prefixes
                    formatted_page = re.sub(r'^[^\#]*', '', formatted_page, flags=re.MULTILINE)
                    formatted_parts.append(formatted_page)
                    formatted_parts.append("\n")
                else:
                    # Fallback
                    formatted_parts.append(f"\n## Page {page_data['page']}\n\n")
                    formatted_parts.append(format_page_basic(page_text))
                    formatted_parts.append("\n")
        
        formatted = "\n".join(formatted_parts)
    else:
        # Process entire document
        prompt = f"""Format this PDF content into markdown. CRITICAL: Preserve ALL content exactly - do NOT summarize, abbreviate, or omit anything.

Requirements:
1. Title: "# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}"
2. Keep all "## Page X" headings
3. Format lists: "- " for bullets, "1. " for numbered
4. Make task titles bold: **Task X**, **Warm-up Task**
5. Format URLs: [text](url)
6. Add "---" for major breaks
7. CRITICAL: Include ALL text - every word must be preserved
8. Do NOT add "[Continues...]", summaries, or placeholders
9. Preserve all examples, excerpts, citations exactly

PDF Content:
{raw_content}

Return the COMPLETE formatted markdown with ALL content. Start with the title."""
        
        formatted = call_poe_api(prompt, api_key)
    
    if not formatted:
        log("  Using fallback formatting (no LLM)", "WARNING")
        formatted = format_markdown_basic(text_content, images_info, session_num)

    # Call LLM
    formatted = call_poe_api(prompt, api_key)
    
    if formatted:
        # Add image references at the end
        if image_refs:
            formatted += image_refs
        log(f"  ✓ LLM formatting complete ({len(formatted)} characters)")
        return formatted
    else:
        # Fallback to basic formatting
        log("  Using fallback formatting (no LLM)", "WARNING")
        return format_markdown_basic(text_content, images_info, session_num)

def format_markdown_basic(text_content, images_info, session_num):
    """Basic markdown formatting without LLM."""
    md_content = []
    md_content.append(f"# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}\n")
    md_content.append("---\n")
    
    for page_data in text_content:
        md_content.append(f"\n## Page {page_data['page']}\n\n")
        
        text = page_data['text']
        
        # Basic formatting improvements
        text = re.sub(r'^Session (\d+)\s+(.+)$', r'### Session \1: \2', text, flags=re.MULTILINE)
        text = re.sub(r'^Learning Outcomes:\s*$', r'**Learning Outcomes:**', text, flags=re.MULTILINE)
        text = re.sub(r'^(Task \d+)', r'**\1**', text, flags=re.MULTILINE)
        text = re.sub(r'^(Warm-up Task)', r'**\1**', text, flags=re.MULTILINE)
        text = re.sub(r'^•\s+', r'- ', text, flags=re.MULTILINE)
        text = re.sub(r'(https?://[^\s\)]+)', r'[\1](\1)', text)
        
        md_content.append(text)
        md_content.append("\n")
    
    # Add images
    if images_info:
        md_content.append("\n---\n\n## Images and Charts\n\n")
        for img_info in images_info:
            session_folder = Path(img_info['path']).parent.name
            rel_path = f"images/{session_folder}/{img_info['filename']}"
            md_content.append(f"### Page {img_info['page']}\n\n")
            md_content.append(f"![Page {img_info['page']}]({rel_path})\n\n")
    
    return "\n".join(md_content)

def process_single_pdf(pdf_path, output_md_dir, output_img_dir, api_key):
    """Process a single PDF file."""
    pdf_path = Path(pdf_path)
    log(f"\n{'='*70}")
    log(f"PROCESSING: {pdf_path.name}")
    log(f"{'='*70}")
    
    # Extract session number
    session_match = re.search(r'Session (\d+)', pdf_path.stem)
    session_num = session_match.group(1) if session_match else "X"
    log(f"Session number: {session_num}")
    
    # Extract images
    session_name = pdf_path.stem.replace('_STUDENT version', '').replace('_STUDENT Version', '')
    img_output_dir = Path(output_img_dir) / session_name
    images_info = extract_images_from_pdf(pdf_path, img_output_dir)
    log(f"✓ Extracted {len(images_info)} page images")
    
    # Extract text
    text_content = extract_text_with_structure(pdf_path)
    if not text_content:
        log(f"✗ Failed to extract text from {pdf_path.name}", "ERROR")
        return False
    
    log(f"✓ Extracted text from {len(text_content)} pages")
    
    # Format with LLM
    md_content = format_markdown_with_llm(text_content, images_info, api_key, session_num)
    
    # Save markdown
    md_filename = pdf_path.stem + ".md"
    md_path = Path(output_md_dir) / md_filename
    
    log(f"Saving markdown to: {md_path.name}")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    log(f"✓ Created markdown file: {md_path} ({len(md_content)} characters)")
    log(f"✓ Processed {len(images_info)} images to {img_output_dir}")
    
    return True

def get_user_feedback(pdf_name, auto_continue=False):
    """Ask user for feedback before proceeding."""
    print(f"\n{'='*70}")
    print(f"Completed processing: {pdf_name}")
    print(f"{'='*70}")
    
    if auto_continue:
        log("Auto-continuing to next PDF (non-interactive mode)")
        return '1'
    
    print("\nOptions:")
    print("1. Continue to next PDF")
    print("2. Review and provide feedback")
    print("3. Skip remaining PDFs")
    print("4. Exit")
    
    try:
        while True:
            choice = input("\nEnter your choice (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return choice
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    except (EOFError, KeyboardInterrupt):
        # Handle non-interactive mode
        log("Non-interactive mode detected, auto-continuing", "WARNING")
        return '1'

def main():
    global LOG_FILE
    
    base_dir = Path("/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026")
    pdf_dir = base_dir / "Materials" / "studentPDFs"
    md_dir = base_dir / "Materials" / "md"
    img_dir = base_dir / "Materials" / "md" / "images"
    log_file_path = base_dir / "process.log"
    
    # Initialize log file
    LOG_FILE = open(log_file_path, 'w', encoding='utf-8')
    log(f"Starting PDF processing session")
    log(f"PDF directory: {pdf_dir}")
    log(f"Output MD directory: {md_dir}")
    log(f"Output images directory: {img_dir}")
    
    # Ensure directories exist
    md_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)
    
    # Get API key
    api_key = get_poe_api_key()
    if api_key:
        log(f"✓ Found Poe API key")
    else:
        log("⚠ No Poe API key found - will use basic formatting", "WARNING")
    
    # Get all PDF files
    pdf_files = sorted(list(pdf_dir.glob("*.pdf")))
    
    if not pdf_files:
        log(f"✗ No PDF files found in {pdf_dir}", "ERROR")
        LOG_FILE.close()
        return
    
    log(f"\nFound {len(pdf_files)} PDF files to process:")
    for i, pdf_file in enumerate(pdf_files, 1):
        log(f"  {i}. {pdf_file.name}")
    
    # Process each PDF one at a time
    processed = 0
    for i, pdf_file in enumerate(pdf_files, 1):
        log(f"\n{'#'*70}")
        log(f"Processing PDF {i}/{len(pdf_files)}")
        log(f"{'#'*70}")
        
        success = process_single_pdf(pdf_file, md_dir, img_dir, api_key)
        
        if success:
            processed += 1
            log(f"✓ Successfully processed: {pdf_file.name}")
        else:
            log(f"✗ Failed to process: {pdf_file.name}", "ERROR")
        
        # Ask for feedback
        if i < len(pdf_files):
            # Check if running in non-interactive mode (no TTY)
            auto_mode = not sys.stdin.isatty()
            choice = get_user_feedback(pdf_file.name, auto_continue=auto_mode)
            
            if choice == '2':
                print("\nPlease review the output files and provide any feedback.")
                input("Press Enter when ready to continue...")
            elif choice == '3':
                log("User chose to skip remaining PDFs")
                break
            elif choice == '4':
                log("User chose to exit")
                break
    
    log(f"\n{'='*70}")
    log(f"Processing session complete")
    log(f"Processed: {processed}/{len(pdf_files)} files")
    log(f"{'='*70}")
    
    LOG_FILE.close()
    print(f"\n✓ Processing complete! Check process.log for details.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        if LOG_FILE:
            log("\nProcess interrupted by user", "WARNING")
            LOG_FILE.close()
        sys.exit(1)
    except Exception as e:
        if LOG_FILE:
            log(f"Fatal error: {e}", "ERROR")
            import traceback
            log(traceback.format_exc(), "ERROR")
            LOG_FILE.close()
        raise
