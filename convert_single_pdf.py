#!/usr/bin/env python3
"""
Convert a single PDF to markdown.
"""

import pdfplumber
import sys
import re
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    text_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                text_content.append(f"## Page {page_num}\n\n{text}\n")
    
    return "\n".join(text_content)

def clean_and_format_markdown(text):
    """Clean and format markdown text."""
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove irregular spacing
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def convert_pdf_to_markdown(pdf_path, output_path):
    """Convert PDF to markdown."""
    pdf_path = Path(pdf_path)
    output_path = Path(output_path)
    
    print(f"Converting: {pdf_path.name}")
    
    # Extract text
    raw_text = extract_text_from_pdf(pdf_path)
    if not raw_text:
        print(f"Failed to extract text")
        return False
    
    # Clean and format
    formatted_text = clean_and_format_markdown(raw_text)
    
    # Write to markdown file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(formatted_text)
    
    print(f"✓ Created: {output_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_single_pdf.py <pdf_path> [output_path]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        # Default output: same name as PDF but with .md extension
        output_path = Path(pdf_path).stem + ".md"
    
    if convert_pdf_to_markdown(pdf_path, output_path):
        print(f"Conversion successful!")
    else:
        print(f"Conversion failed!")
        sys.exit(1)
