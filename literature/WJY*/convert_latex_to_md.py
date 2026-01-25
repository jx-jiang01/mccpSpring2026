#!/usr/bin/env python3
"""
Convert LaTeX paper to Markdown format
"""
import re
import sys

def clean_latex_to_markdown(latex_content):
    """Convert LaTeX content to Markdown"""
    
    # Remove LaTeX comments
    content = re.sub(r'%.*', '', latex_content)
    
    # Extract title
    title_match = re.search(r'\\title\{([^}]+)\}', content)
    title = title_match.group(1) if title_match else "Untitled"
    
    # Extract abstract
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ""
    
    # Extract sections
    sections = []
    section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section|\\end\{document\}|$)'
    
    for match in re.finditer(section_pattern, content, re.DOTALL):
        section_title = match.group(1)
        section_content = match.group(2)
        
        # Clean up section content
        section_content = clean_section_content(section_content)
        sections.append((section_title, section_content))
    
    # Build markdown
    md = f"# {title}\n\n"
    
    if abstract:
        md += f"## Abstract\n\n{clean_text(abstract)}\n\n"
    
    for section_title, section_content in sections:
        md += f"## {section_title}\n\n{section_content}\n\n"
    
    return md

def clean_section_content(content):
    """Clean LaTeX commands from section content"""
    # Remove figure environments
    content = re.sub(r'\\begin\{figure[^}]*\}.*?\\end\{figure[^}]*\}', '', content, flags=re.DOTALL)
    
    # Remove equation environments (keep the content)
    content = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', r'\\[\1\\]', content, flags=re.DOTALL)
    
    # Convert subsections
    content = re.sub(r'\\subsection\{([^}]+)\}', r'### \1', content)
    content = re.sub(r'\\subsubsection\{([^}]+)\}', r'#### \1', content)
    
    # Convert paragraphs
    content = re.sub(r'\\paragraph\{([^}]+)\}', r'**\1**', content)
    
    # Remove citations (keep just the text)
    content = re.sub(r'\\cite\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citep\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citet\{[^}]+\}', '[citation]', content)
    
    # Remove labels
    content = re.sub(r'\\label\{[^}]+\}', '', content)
    
    # Remove refs
    content = re.sub(r'\\ref\{[^}]+\}', '[reference]', content)
    
    # Remove emph and textbf
    content = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', content)
    content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', content)
    
    # Remove itemize/enumerate environments (simplify)
    content = re.sub(r'\\begin\{enumerate\}.*?\\end\{enumerate\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\item\s+', '- ', content)
    
    # Clean up whitespace
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = content.strip()
    
    return clean_text(content)

def clean_text(text):
    """Clean LaTeX commands from text"""
    # Remove remaining LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    
    # Clean up special characters
    text = text.replace('~', ' ')
    text = text.replace('\\', '')
    
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    return text.strip()

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "Expert-deploy/arXiv-2508.02929v2/paper.tex"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "FoundationExpert_paper.md"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        latex_content = f.read()
    
    markdown_content = clean_latex_to_markdown(latex_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Converted {input_file} to {output_file}")
