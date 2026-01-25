#!/usr/bin/env python3
"""
Convert LaTeX paper to Markdown format
Adapted for mc-diffusion.tex
"""
import re
import sys

def clean_latex_to_markdown(latex_content):
    """Convert LaTeX content to Markdown"""
    
    # Remove LaTeX comments
    content = re.sub(r'%.*', '', latex_content)
    
    # Extract title
    title_match = re.search(r'\\title\{([^}]+)\}', content)
    title = title_match.group(1).strip() if title_match else "Untitled"
    
    # Extract authors
    authors = []
    author_pattern = r'([A-Za-z]+\s+[A-Za-z]+)\\inst\{[0-9]+\}'
    for match in re.finditer(author_pattern, content):
        authors.append(match.group(1))
    
    # Extract abstract
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ""
    
    # Extract keywords
    keywords_match = re.search(r'\\keywords\{([^}]+)\}', content)
    keywords = keywords_match.group(1) if keywords_match else ""
    
    # Extract sections
    sections = []
    section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section|\\bibliography|\\end\{document\}|$)'
    
    for match in re.finditer(section_pattern, content, re.DOTALL):
        section_title = match.group(1)
        section_content = match.group(2)
        
        # Clean up section content
        section_content = clean_section_content(section_content)
        sections.append((section_title, section_content))
    
    # Build markdown
    md = f"# {title}\n\n"
    
    if authors:
        md += f"**Authors**: {', '.join(authors)}\n\n"
    
    if abstract:
        md += f"## Abstract\n\n{clean_text(abstract)}\n\n"
    
    if keywords:
        md += f"**Keywords**: {clean_text(keywords)}\n\n"
    
    md += "---\n\n"
    
    for section_title, section_content in sections:
        md += f"## {section_title}\n\n{section_content}\n\n"
    
    return md

def clean_section_content(content):
    """Clean LaTeX commands from section content"""
    # Remove figure environments (keep caption text if needed)
    content = re.sub(r'\\begin\{figure[^}]*\}.*?\\caption\{([^}]+)\}.*?\\end\{figure[^}]*\}', 
                     r'[Figure: \1]', content, flags=re.DOTALL)
    
    # Remove table environments
    content = re.sub(r'\\begin\{table[^}]*\}.*?\\end\{table[^}]*\}', '[Table]', content, flags=re.DOTALL)
    
    # Remove equation environments (keep some content)
    content = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', r'\\[\1\\]', content, flags=re.DOTALL)
    
    # Convert subsections
    content = re.sub(r'\\subsection\{([^}]+)\}', r'### \1', content)
    content = re.sub(r'\\subsubsection\{([^}]+)\}', r'#### \1', content)
    
    # Convert paragraphs
    content = re.sub(r'\\paragraph\{([^}]+)\}', r'**\1**', content)
    
    # Handle itemize environments (convert to markdown lists)
    def replace_itemize(match):
        items = re.findall(r'\\item\s+([^\n]+(?:\n(?!\\item)[^\n]+)*)', match.group(0))
        return '\n'.join(['- ' + clean_text(item.strip()) for item in items]) + '\n\n'
    
    content = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', replace_itemize, content, flags=re.DOTALL)
    
    # Handle enumerate environments
    def replace_enumerate(match):
        items = re.findall(r'\\item\s+([^\n]+(?:\n(?!\\item)[^\n]+)*)', match.group(0))
        return '\n'.join([f'{i+1}. ' + clean_text(item.strip()) for i, item in enumerate(items)]) + '\n\n'
    
    content = re.sub(r'\\begin\{enumerate\}.*?\\end\{enumerate\}', replace_enumerate, content, flags=re.DOTALL)
    
    # Handle item commands (standalone)
    content = re.sub(r'\\item\s+', '- ', content)
    
    # Remove citations (keep just the text)
    content = re.sub(r'\\cite\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citep\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citet\{[^}]+\}', '[citation]', content)
    content = re.sub(r'~\\cite\{[^}]+\}', ' [citation]', content)
    
    # Remove labels
    content = re.sub(r'\\label\{[^}]+\}', '', content)
    
    # Remove refs (replace with readable text)
    content = re.sub(r'Figure~\\ref\{([^}]+)\}', 'Figure [reference]', content)
    content = re.sub(r'Table~\\ref\{([^}]+)\}', 'Table [reference]', content)
    content = re.sub(r'\\ref\{[^}]+\}', '[reference]', content)
    
    # Remove emph and textbf (convert to markdown)
    content = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', content)
    content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', content)
    
    # Handle math mode (simplify)
    content = re.sub(r'\$([^\$]+)\$', r'[\1]', content)
    content = re.sub(r'\\\[(.*?)\\\]', r'[\1]', content, flags=re.DOTALL)
    
    # Remove minipage environments
    content = re.sub(r'\\begin\{minipage\}.*?\\end\{minipage\}', '', content, flags=re.DOTALL)
    
    # Remove includegraphics
    content = re.sub(r'\\includegraphics\[[^\]]*\]\{[^}]+\}', '[Image]', content)
    
    # Remove other common LaTeX commands
    content = re.sub(r'\\centering', '', content)
    content = re.sub(r'\\vspace\{[^}]+\}', '\n', content)
    content = re.sub(r'\\hfill', ' ', content)
    content = re.sub(r'\\newpage', '\n\n', content)
    
    # Clean up whitespace
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = content.strip()
    
    return clean_text(content)

def clean_text(text):
    """Clean LaTeX commands from text"""
    # Remove remaining LaTeX commands with braces
    text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', text)
    
    # Remove standalone LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    
    # Clean up special characters
    text = text.replace('~', ' ')
    text = text.replace('\\&', '&')
    text = text.replace('\\%', '%')
    text = text.replace('\\$', '$')
    text = text.replace('\\#', '#')
    text = text.replace('\\_', '_')
    text = text.replace('\\{', '{')
    text = text.replace('\\}', '}')
    
    # Clean up whitespace
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    return text.strip()

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "extracted/mc-diffusion.tex"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "mc-diffusion_paper.md"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        latex_content = f.read()
    
    markdown_content = clean_latex_to_markdown(latex_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Converted {input_file} to {output_file}")
