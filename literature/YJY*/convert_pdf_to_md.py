#!/usr/bin/env python3
"""
Convert PDF files to Markdown format for analysis.
"""

import pymupdf  # PyMuPDF (fitz)
import os
import sys
from pathlib import Path

def pdf_to_markdown(pdf_path, md_path):
    """Convert PDF file to Markdown format."""
    try:
        doc = pymupdf.open(pdf_path)
        markdown_content = []
        
        # Add title from PDF metadata or filename
        metadata = doc.metadata
        title = metadata.get('title', '').strip()
        if title:
            markdown_content.append(f"# {title}\n")
        
        # Extract text from each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            
            # Add page break marker
            markdown_content.append(f"\n## Page {page_num + 1}\n\n")
            markdown_content.append(text)
            markdown_content.append("\n\n")
        
        doc.close()
        
        # Write to markdown file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        print(f"✓ Converted {pdf_path} to {md_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {pdf_path}: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    
    # Find all PDF files in the directory
    pdf_files = list(script_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        sys.exit(1)
    
    print(f"Found {len(pdf_files)} PDF file(s) to convert:\n")
    
    for pdf_file in pdf_files:
        # Create markdown filename
        md_file = pdf_file.with_suffix('.md')
        pdf_to_markdown(pdf_file, md_file)
