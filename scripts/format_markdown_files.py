#!/usr/bin/env python3
"""
Format markdown files extracted from PDFs to ensure proper structure,
headings, lists, and formatting. Uses AI-style pattern matching to improve
the markdown structure.
"""

import re
from pathlib import Path

def format_markdown_content(content):
    """Format markdown content with proper structure."""
    
    # Add main title at the beginning if not present
    if not content.startswith('#'):
        # Extract course title from first page
        lines = content.split('\n')
        if len(lines) > 2 and 'MCCP6020' in lines[2]:
            title_line = lines[2]
            content = f"# {title_line}\n\n---\n\n" + content
    
    # Fix session titles - convert "Session X" to proper heading
    content = re.sub(r'^## Page \d+\n\nMCCP6020.*?\n(Session \d+ [^\n]+)', r'## Page \1\n\n### \1', content, flags=re.MULTILINE)
    
    # Fix "Learning Outcomes:" to bold
    content = re.sub(r'^Learning Outcomes:\s*$', r'**Learning Outcomes:**', content, flags=re.MULTILINE)
    
    # Fix bullet points - convert • to -
    content = re.sub(r'^•\s+', r'- ', content, flags=re.MULTILINE)
    
    # Fix numbered lists that are broken across lines
    content = re.sub(r'^(\d+)\.\s*\n\n([^\n]+)$', r'\1. \2', content, flags=re.MULTILINE)
    
    # Fix "Task X" to bold
    content = re.sub(r'^(Task \d+)', r'**\1**', content, flags=re.MULTILINE)
    
    # Fix "Warm-up Task" to bold
    content = re.sub(r'^(Warm-up Task)', r'**\1**', content, flags=re.MULTILINE)
    
    # Add horizontal rules before major sections
    content = re.sub(r'\n(## Page \d+)\n', r'\n---\n\n\1\n', content)
    
    # Fix section titles that should be headings
    section_titles = [
        r'Structure of a Thesis/Journal Article',
        r'Introducing Your Research',
        r'Claiming Centrality of Your Research Topic',
        r'Doing Things with Nouns \(Nominalization\)',
        r'Independent Language Learning',
    ]
    
    for title in section_titles:
        # Make sure these are proper headings when they appear after page breaks
        pattern = rf'\n({title})\n'
        replacement = rf'\n### \1\n'
        content = re.sub(pattern, replacement, content)
    
    # Fix URLs - make them proper markdown links
    url_pattern = r'(https?://[^\s\)]+)'
    content = re.sub(url_pattern, r'[\1](\1)', content)
    
    # Remove excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Fix table-like structures (basic attempt)
    # This is a simplified version - full table formatting would be more complex
    
    return content

def format_file(file_path):
    """Format a single markdown file."""
    print(f"Formatting: {file_path.name}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatted = format_markdown_content(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted)
        
        print(f"✓ Formatted: {file_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error formatting {file_path.name}: {e}")
        return False

def main():
    base_dir = Path("/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026")
    md_dir = base_dir / "Materials" / "md"
    
    md_files = list(md_dir.glob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {md_dir}")
        return
    
    print(f"Found {len(md_files)} markdown files to format\n")
    
    success_count = 0
    for md_file in sorted(md_files):
        if format_file(md_file):
            success_count += 1
        print()
    
    print(f"\nFormatting complete: {success_count}/{len(md_files)} files formatted successfully")
    print("\nNote: Files have been formatted with basic structure improvements.")
    print("Please review and manually adjust formatting as needed, especially for:")
    print("- Complex tables")
    print("- Special formatting")
    print("- Image references")

if __name__ == "__main__":
    main()
