#!/usr/bin/env python3
"""
Convert LaTeX papers to Markdown format for WYQin papers
Handles both single-file and multi-file LaTeX documents
"""
import re
import sys
import os
from pathlib import Path

def resolve_inputs(content, base_dir):
    """Resolve \input{} commands by reading the referenced files"""
    input_pattern = r'\\input\{([^}]+)\}'
    
    def replace_input(match):
        filename = match.group(1)
        # Remove .tex extension if present (LaTeX allows it either way)
        if not filename.endswith('.tex'):
            filename += '.tex'
        
        filepath = base_dir / filename
        if filepath.exists():
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    return f.read()
            except:
                return match.group(0)  # Return original if can't read
        return match.group(0)  # Return original if file doesn't exist
    
    # Recursively resolve inputs (limit depth to avoid infinite loops)
    max_iterations = 10
    for _ in range(max_iterations):
        new_content = re.sub(input_pattern, replace_input, content)
        if new_content == content:
            break
        content = new_content
    
    return content

def clean_latex_to_markdown(latex_content, base_dir=None):
    """Convert LaTeX content to Markdown"""
    
    # Resolve input commands if base_dir is provided
    if base_dir:
        latex_content = resolve_inputs(latex_content, Path(base_dir))
    
    # Remove LaTeX comments
    content = re.sub(r'%.*', '', latex_content)
    
    # Extract title
    title_match = re.search(r'\\title\{([^}]+)\}', content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else "Untitled"
    title = clean_text(title)
    
    # Extract authors
    authors = []
    # Try different author patterns
    author_patterns = [
        r'\\author\{([^}]+)\}',
        r'([A-Za-z]+\s+[A-Za-z]+)\\inst\{[0-9]+\}',
    ]
    for pattern in author_patterns:
        matches = re.finditer(pattern, content, re.DOTALL)
        for match in matches:
            author_text = match.group(1)
            # Clean up author text
            author_text = re.sub(r'\\thanks\{[^}]+\}', '', author_text)
            author_text = clean_text(author_text)
            if author_text and author_text not in authors:
                authors.append(author_text)
    
    # Extract affiliations
    affiliation_match = re.search(r'\\affiliations?\{([^}]+)\}', content, re.DOTALL)
    affiliation = clean_text(affiliation_match.group(1)) if affiliation_match else ""
    
    # Extract abstract
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else ""
    
    # Extract sections
    sections = []
    section_pattern = r'\\section\{([^}]+)\}(.*?)(?=\\section|\\subsection|\\bibliography|\\end\{document\}|$)'
    
    for match in re.finditer(section_pattern, content, re.DOTALL):
        section_title = match.group(1)
        section_content = match.group(2)
        
        # Clean up section content
        section_content = clean_section_content(section_content)
        sections.append((section_title, section_content))
    
    # Extract subsections that don't belong to sections
    subsection_pattern = r'\\subsection\{([^}]+)\}(.*?)(?=\\section|\\subsection|\\bibliography|\\end\{document\}|$)'
    
    # Build markdown
    md = f"# {title}\n\n"
    
    if authors:
        md += f"**Authors**: {', '.join(authors)}\n\n"
    
    if affiliation:
        md += f"**Affiliation**: {affiliation}\n\n"
    
    if abstract:
        md += f"## Abstract\n\n{clean_text(abstract)}\n\n"
    
    md += "---\n\n"
    
    for section_title, section_content in sections:
        md += f"## {section_title}\n\n{section_content}\n\n"
    
    return md

def clean_section_content(content):
    """Clean LaTeX commands from section content"""
    # Convert subsections
    content = re.sub(r'\\subsection\{([^}]+)\}', r'### \1', content)
    content = re.sub(r'\\subsubsection\{([^}]+)\}', r'#### \1', content)
    
    # Handle itemize environments
    def replace_itemize(match):
        items = re.findall(r'\\item\s+([^\n]+(?:\n(?!\\item|\\end)[^\n]+)*)', match.group(0), re.DOTALL)
        result = '\n'.join(['- ' + clean_text(item.strip()) for item in items if item.strip()])
        return result + '\n\n' if result else ''
    
    content = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', replace_itemize, content, flags=re.DOTALL)
    
    # Handle enumerate environments
    def replace_enumerate(match):
        items = re.findall(r'\\item\s+([^\n]+(?:\n(?!\\item|\\end)[^\n]+)*)', match.group(0), re.DOTALL)
        result = '\n'.join([f'{i+1}. ' + clean_text(item.strip()) for i, item in enumerate(items) if item.strip()])
        return result + '\n\n' if result else ''
    
    content = re.sub(r'\\begin\{enumerate\}.*?\\end\{enumerate\}', replace_enumerate, content, flags=re.DOTALL)
    
    # Handle standalone item commands
    content = re.sub(r'\\item\s+', '- ', content)
    
    # Remove figure environments (keep caption)
    content = re.sub(r'\\begin\{figure[^}]*\}.*?\\caption\{([^}]+)\}.*?\\end\{figure[^}]*\}', 
                     r'[Figure: \1]', content, flags=re.DOTALL)
    
    # Remove table environments
    content = re.sub(r'\\begin\{table[^}]*\}.*?\\end\{table[^}]*\}', '[Table]', content, flags=re.DOTALL)
    
    # Remove algorithm environments
    content = re.sub(r'\\begin\{algorithm[^}]*\}.*?\\end\{algorithm[^}]*\}', '[Algorithm]', content, flags=re.DOTALL)
    
    # Remove equation environments (keep content)
    content = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', r'[Equation: \1]', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{align\}(.*?)\\end\{align\}', r'[Equation]', content, flags=re.DOTALL)
    
    # Remove citations (keep just placeholder)
    content = re.sub(r'\\cite\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citep\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citet\{[^}]+\}', '[citation]', content)
    content = re.sub(r'\\citet\*\{[^}]+\}', '[citation]', content)
    
    # Remove labels and refs
    content = re.sub(r'\\label\{[^}]+\}', '', content)
    content = re.sub(r'\\ref\{[^}]+\}', '[reference]', content)
    
    # Convert emphasis
    content = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', content)
    content = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', content)
    content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', content)
    content = re.sub(r'\\underline\{([^}]+)\}', r'**\1**', content)
    
    # Handle math mode (simplify)
    content = re.sub(r'\$([^\$]+)\$', r'[\1]', content)
    content = re.sub(r'\\\[(.*?)\\\]', r'[\1]', content, flags=re.DOTALL)
    
    # Remove other LaTeX commands
    content = re.sub(r'\\includegraphics\[[^\]]*\]\{[^}]+\}', '[Image]', content)
    content = re.sub(r'\\centering', '', content)
    content = re.sub(r'\\vspace\{[^}]+\}', '\n', content)
    content = re.sub(r'\\newpage', '\n\n', content)
    
    return clean_text(content)

def clean_text(text):
    """Clean LaTeX commands from text"""
    # Remove remaining LaTeX commands with braces (but preserve content)
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
    if len(sys.argv) < 3:
        print("Usage: python convert_latex_to_md.py <input_tex_file> <output_md_file> [base_dir]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    base_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(input_file).parent
    
    with open(input_file, 'r', encoding='utf-8') as f:
        latex_content = f.read()
    
    markdown_content = clean_latex_to_markdown(latex_content, base_dir)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Converted {input_file} to {output_file}")
