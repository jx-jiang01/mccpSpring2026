#!/usr/bin/env python3
"""
Process PDFs with OCR/AI to extract images, charts, and generate properly formatted markdown.
Uses Poe API for LLM processing to improve markdown structure and content.
"""

import os
import sys
import pdfplumber
from pdf2image import convert_from_path
from pathlib import Path
import requests
import json
import base64
from PIL import Image
import io
import re

# Read Poe API key
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
    """Extract images and charts from PDF pages."""
    images_info = []
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting images from: {pdf_path.name}")
    
    try:
        # Convert PDF pages to images
        images = convert_from_path(pdf_path, dpi=300)
        
        # Also extract embedded images from PDF
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                # Extract images from page
                if hasattr(page, 'images') and page.images:
                    for img_idx, img in enumerate(page.images):
                        # Try to extract image
                        try:
                            # Get image from page
                            bbox = (img['x0'], img['top'], img['x1'], img['bottom'])
                            # Note: pdfplumber doesn't directly extract images, we'll use page images
                            pass
                        except Exception as e:
                            print(f"  Warning: Could not extract image {img_idx} from page {page_num}: {e}")
        
        # Save page images
        for page_num, img in enumerate(images, 1):
            img_filename = f"page_{page_num:03d}.png"
            img_path = output_dir / img_filename
            img.save(img_path, 'PNG')
            images_info.append({
                'page': page_num,
                'path': str(img_path),
                'filename': img_filename
            })
            print(f"  Saved page {page_num} image: {img_filename}")
        
        return images_info
    except Exception as e:
        print(f"Error extracting images: {e}")
        return []

def extract_text_with_structure(pdf_path):
    """Extract text from PDF with structure preservation."""
    text_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    text_content.append({
                        'page': page_num,
                        'text': text
                    })
    except Exception as e:
        print(f"Error extracting text: {e}")
        return []
    
    return text_content

def call_poe_api(prompt, api_key):
    """Call Poe API to process content with LLM using OpenAI-compatible API."""
    if not api_key:
        print("Warning: No Poe API key found. Skipping LLM processing.")
        return None
    
    try:
        # Poe API is OpenAI-compatible
        url = "https://api.poe.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "Claude-3.5-Sonnet",  # Available models on Poe
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 16000,
            "temperature": 0.3
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('choices', [{}])[0].get('message', {}).get('content', '')
        else:
            print(f"Poe API error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error calling Poe API: {e}")
        print("Note: Using fallback formatting instead of LLM processing")
        return None

def format_markdown_with_llm(text_content, images_info, api_key, session_num):
    """Use LLM to format markdown content properly, processing in chunks."""
    
    # First, build the complete raw markdown with all content
    full_raw_md = []
    full_raw_md.append(f"# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}\n")
    full_raw_md.append("---\n")
    
    for page_data in text_content:
        full_raw_md.append(f"\n## Page {page_data['page']}\n\n")
        full_raw_md.append(page_data['text'])
        full_raw_md.append("\n")
    
    # Add image references at the end
    if images_info:
        full_raw_md.append("\n---\n\n## Images and Charts\n\n")
        for img_info in images_info:
            session_folder = Path(img_info['path']).parent.name
            rel_path = f"images/{session_folder}/{img_info['filename']}"
            full_raw_md.append(f"### Page {img_info['page']}\n\n")
            full_raw_md.append(f"![Page {img_info['page']}]({rel_path})\n\n")
    
    raw_content = "\n".join(full_raw_md)
    
    # Process with LLM in chunks if content is too long
    max_chunk_size = 10000
    
    if len(raw_content) > max_chunk_size:
        # Process page by page
        formatted_parts = []
        formatted_parts.append(f"# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}\n")
        formatted_parts.append("---\n")
        
        for page_data in text_content:
            page_text = page_data['text']
            prompt = f"""Format the following page content into proper markdown. Preserve ALL text exactly - do NOT summarize or omit anything.

Requirements:
- Keep "## Page {page_data['page']}" as heading
- Format lists properly (- for bullets, 1. for numbered)
- Make task titles bold (**Task X**)
- Format URLs as [text](url)
- Preserve all content exactly

Page Content:
{page_text}

Return formatted markdown with ALL content preserved:"""
            
            formatted_page = call_poe_api(prompt, api_key)
            if formatted_page:
                formatted_parts.append(f"## Page {page_data['page']}\n\n{formatted_page}\n")
            else:
                # Fallback: basic formatting
                formatted_parts.append(f"## Page {page_data['page']}\n\n{format_page_basic(page_text)}\n")
        
        # Add images
        if images_info:
            formatted_parts.append("\n---\n\n## Images and Charts\n\n")
            for img_info in images_info:
                session_folder = Path(img_info['path']).parent.name
                rel_path = f"images/{session_folder}/{img_info['filename']}"
                formatted_parts.append(f"### Page {img_info['page']}\n\n")
                formatted_parts.append(f"![Page {img_info['page']}]({rel_path})\n\n")
        
        return "\n".join(formatted_parts)
    else:
        # Process entire document
        prompt = f"""Format the following markdown content. CRITICAL: Preserve ALL content exactly - do NOT summarize, abbreviate, or omit anything.

Requirements:
1. Keep the title "# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES SESSION {session_num}"
2. Keep all "## Page X" headings
3. Format lists properly (- for bullets, 1. for numbered)
4. Make task titles bold (**Task X**, **Warm-up Task**)
5. Format URLs as [text](url)
6. Add proper spacing (--- for major breaks)
7. CRITICAL: Include ALL text - every word must be preserved
8. Do NOT add summaries or "[Continues...]" - include ALL content

Content to format:
{raw_content[:max_chunk_size]}

Return the complete formatted markdown with ALL content preserved:"""

        formatted = call_poe_api(prompt, api_key)
        if formatted:
            return formatted
        else:
            return format_markdown_basic(text_content, images_info)

def format_page_basic(text):
    """Basic formatting for a single page."""
    # Fix task titles
    text = re.sub(r'^(Task \d+)', r'**\1**', text, flags=re.MULTILINE)
    text = re.sub(r'^(Warm-up Task)', r'**\1**', text, flags=re.MULTILINE)
    # Fix bullet points
    text = re.sub(r'^•\s+', r'- ', text, flags=re.MULTILINE)
    # Fix URLs
    text = re.sub(r'(https?://[^\s\)]+)', r'[\1](\1)', text)
    return text

def format_markdown_basic(text_content, images_info):
    """Basic markdown formatting without LLM."""
    md_content = []
    
    # Add title
    md_content.append("# MCCP6020 ADVANCED ENGLISH FOR ACADEMIC PURPOSES\n")
    md_content.append("---\n")
    
    for page_data in text_content:
        md_content.append(f"\n## Page {page_data['page']}\n")
        
        text = page_data['text']
        
        # Basic formatting improvements
        # Fix session titles
        text = re.sub(r'^Session (\d+)\s+(.+)$', r'### Session \1: \2', text, flags=re.MULTILINE)
        
        # Fix learning outcomes
        text = re.sub(r'^Learning Outcomes:\s*$', r'**Learning Outcomes:**', text, flags=re.MULTILINE)
        
        # Fix task titles
        text = re.sub(r'^(Task \d+)', r'**\1**', text, flags=re.MULTILINE)
        text = re.sub(r'^(Warm-up Task)', r'**\1**', text, flags=re.MULTILINE)
        
        # Fix bullet points
        text = re.sub(r'^•\s+', r'- ', text, flags=re.MULTILINE)
        
        # Fix URLs
        text = re.sub(r'(https?://[^\s\)]+)', r'[\1](\1)', text)
        
        md_content.append(text)
        md_content.append("\n")
    
    # Add images section
    if images_info:
        md_content.append("\n---\n\n## Images and Charts\n\n")
        for img_info in images_info:
            md_content.append(f"### Page {img_info['page']}\n\n")
            md_content.append(f"![Page {img_info['page']}]({img_info['filename']})\n\n")
    
    return "\n".join(md_content)

def process_pdf(pdf_path, output_md_dir, output_img_dir, api_key):
    """Process a single PDF file."""
    pdf_path = Path(pdf_path)
    print(f"\n{'='*60}")
    print(f"Processing: {pdf_path.name}")
    print(f"{'='*60}")
    
    # Extract images
    session_name = pdf_path.stem.replace('_STUDENT version', '').replace('_STUDENT Version', '')
    img_output_dir = Path(output_img_dir) / session_name
    images_info = extract_images_from_pdf(pdf_path, img_output_dir)
    
    # Extract text
    text_content = extract_text_with_structure(pdf_path)
    
    if not text_content:
        print(f"Warning: No text extracted from {pdf_path.name}")
        return False
    
    # Extract session number from filename
    session_match = re.search(r'Session (\d+)', pdf_path.stem)
    session_num = session_match.group(1) if session_match else "X"
    
    # Format with LLM
    md_content = format_markdown_with_llm(text_content, images_info, api_key, session_num)
    
    # Save markdown
    md_filename = pdf_path.stem + ".md"
    md_path = Path(output_md_dir) / md_filename
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"✓ Created: {md_path}")
    print(f"✓ Extracted {len(images_info)} images to {img_output_dir}")
    
    return True

def main():
    base_dir = Path("/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026")
    pdf_dir = base_dir / "Materials" / "studentPDFs"
    md_dir = base_dir / "Materials" / "md"
    img_dir = base_dir / "Materials" / "md" / "images"
    
    # Ensure directories exist
    md_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)
    
    # Get API key
    api_key = get_poe_api_key()
    if api_key:
        print(f"✓ Found Poe API key")
    else:
        print("⚠ No Poe API key found - will use basic formatting")
    
    # Get all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return
    
    print(f"\nFound {len(pdf_files)} PDF files to process\n")
    
    # Process each PDF
    success_count = 0
    for pdf_file in sorted(pdf_files):
        if process_pdf(pdf_file, md_dir, img_dir, api_key):
            success_count += 1
        print()  # Blank line between files
    
    print(f"\n{'='*60}")
    print(f"Processing complete: {success_count}/{len(pdf_files)} files processed")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
