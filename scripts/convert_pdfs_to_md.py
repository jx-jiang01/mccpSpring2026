#!/usr/bin/env python3
"""
Convert PDF files to markdown format with AI-assisted formatting.
Ensures no content is lost and formats properly.
"""

import os
import sys
import pdfplumber
from pathlib import Path
import re

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file with structure preservation."""
    text_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    text_content.append(f"## Page {page_num}\n\n{text}\n")
    except Exception as e:
        print(f"Error extracting from {pdf_path}: {e}")
        return None
    
    return "\n".join(text_content)

def clean_and_format_markdown(text):
    """Basic cleaning and formatting of markdown text."""
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Fix common formatting issues
    text = re.sub(r'([.!?])\s+([A-Z])', r'\1\n\n\2', text)  # Add paragraph breaks after sentences
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)  # Remove triple+ newlines
    
    return text.strip()

def convert_pdf_to_markdown(pdf_path, output_path):
    """Convert a PDF file to markdown format."""
    print(f"Converting: {pdf_path}")
    
    # Extract text from PDF
    raw_text = extract_text_from_pdf(pdf_path)
    if not raw_text:
        print(f"Failed to extract text from {pdf_path}")
        return False
    
    # Clean and format
    formatted_text = clean_and_format_markdown(raw_text)
    
    # Write to markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted_text)
        print(f"✓ Created: {output_path}")
        return True
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        return False

def main():
    # Define paths
    base_dir = Path("/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026")
    pdf_dir = base_dir / "Materials" / "studentPDFs"
    md_dir = base_dir / "Materials" / "md"
    
    # Ensure output directory exists
    md_dir.mkdir(parents=True, exist_ok=True)
    
    # Get all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return
    
    print(f"Found {len(pdf_files)} PDF files to convert\n")
    
    # Convert each PDF
    success_count = 0
    for pdf_file in sorted(pdf_files):
        # Generate output filename
        md_filename = pdf_file.stem + ".md"
        md_path = md_dir / md_filename
        
        if convert_pdf_to_markdown(pdf_file, md_path):
            success_count += 1
        print()  # Blank line between files
    
    print(f"\nConversion complete: {success_count}/{len(pdf_files)} files converted successfully")

if __name__ == "__main__":
    main()
