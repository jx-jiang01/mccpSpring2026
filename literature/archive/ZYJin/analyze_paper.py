#!/usr/bin/env python3
"""
Script to analyze the ZYJin paper HTML and generate macro-level structure analysis reports.
"""

import re
from bs4 import BeautifulSoup
from html import unescape
import json

def clean_text(text):
    """Clean and normalize text from HTML."""
    if not text:
        return ""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Decode HTML entities
    text = unescape(text)
    return text.strip()

def extract_text_from_element(elem):
    """Extract clean text from an HTML element, handling math notation."""
    if not elem:
        return ""
    
    # Get all text, but skip script and style tags
    for script in elem(["script", "style"]):
        script.decompose()
    
    text = elem.get_text(separator=' ', strip=True)
    return clean_text(text)

def extract_paragraphs(section):
    """Extract paragraphs from a section."""
    paragraphs = []
    para_elements = section.find_all('p', class_='ltx_p')
    
    for para in para_elements:
        text = extract_text_from_element(para)
        if text and len(text) > 20:  # Filter out very short fragments
            paragraphs.append(text)
    
    return paragraphs

def extract_sections(html_file):
    """Extract all sections from the HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract metadata
    title_elem = soup.find('h1', class_='ltx_title_document')
    title = title_elem.get_text(strip=True) if title_elem else "Unknown Title"
    
    authors = []
    author_elems = soup.find_all('span', class_='ltx_personname')
    for author in author_elems:
        authors.append(author.get_text(strip=True))
    
    abstract_elem = soup.find('div', class_='ltx_abstract')
    abstract = ""
    if abstract_elem:
        abstract_para = abstract_elem.find('p', class_='ltx_p')
        if abstract_para:
            abstract = extract_text_from_element(abstract_para)
    
    # Extract sections
    sections = []
    section_elems = soup.find_all('section', class_='ltx_section')
    
    for section in section_elems:
        section_id = section.get('id', '')
        section_title_elem = section.find('h2', class_='ltx_title_section')
        
        if section_title_elem:
            section_title = extract_text_from_element(section_title_elem)
            paragraphs = extract_paragraphs(section)
            
            sections.append({
                'id': section_id,
                'title': section_title,
                'paragraphs': paragraphs
            })
    
    return {
        'title': title,
        'authors': authors,
        'abstract': abstract,
        'sections': sections
    }

def generate_markdown_report(paper_data, output_file):
    """Generate markdown analysis report similar to KellerInsights.md."""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Header
        f.write(f"# {paper_data['title']} Macro-Level Structure Analysis\n\n")
        f.write(f"**Paper Title**: {paper_data['title']}\n")
        f.write(f"**Authors**: {', '.join(paper_data['authors'])}\n")
        f.write(f"**Field**: Mathematics / Optimization Theory\n")
        f.write(f"**Structure Type**: Theoretical Mathematics Paper\n\n")
        f.write("---\n\n")
        
        # Abstract
        f.write("## Abstract\n\n")
        f.write(f"{paper_data['abstract']}\n\n")
        f.write("---\n\n")
        
        # Overall Assessment
        f.write("## Overall Macro-Level Assessment\n\n")
        f.write("### Structural Framework\n")
        section_titles = [s['title'] for s in paper_data['sections']]
        f.write(f"**Structure**: {' → '.join(section_titles)}\n")
        f.write(f"- **Total Sections**: {len(paper_data['sections'])}\n")
        f.write("- **Citation Style**: Standard mathematical notation\n")
        f.write("- **Disciplinary Conventions**: Heavy emphasis on theoretical proofs, mathematical formalism, and characterization theorems\n")
        f.write("- **Rhetorical Style**: Definition-theorem-proof structure with strong theoretical justification\n\n")
        
        # Section-by-section analysis
        f.write("## Section-by-Section Macro Analysis\n\n")
        
        for i, section in enumerate(paper_data['sections'], 1):
            f.write(f"### Section {i}: {section['title']}\n\n")
            
            if section['paragraphs']:
                # Extract key excerpts (first few paragraphs)
                key_paragraphs = section['paragraphs'][:3]
                
                f.write("#### Key Content\n")
                f.write(f"**Paragraphs**: {len(section['paragraphs'])} paragraphs\n")
                f.write("**Strengths**:\n")
                
                # Analyze based on section title
                if 'Introduction' in section['title']:
                    f.write("- Establishes problem context and motivation\n")
                    f.write("- Defines key mathematical concepts\n")
                    f.write("- Presents main research question\n")
                elif 'Preliminaries' in section['title']:
                    f.write("- Provides necessary mathematical background\n")
                    f.write("- Establishes notation and definitions\n")
                    f.write("- Sets up theoretical framework\n")
                elif 'Characterization' in section['title'] or 'Tightness' in section['title']:
                    f.write("- Presents main theoretical results\n")
                    f.write("- Provides characterization theorems\n")
                    f.write("- Establishes necessary and sufficient conditions\n")
                elif 'Proof' in section['title']:
                    f.write("- Provides rigorous mathematical proofs\n")
                    f.write("- Demonstrates theoretical validity\n")
                    f.write("- Uses standard proof techniques\n")
                elif 'Example' in section['title']:
                    f.write("- Illustrates theoretical concepts\n")
                    f.write("- Provides concrete applications\n")
                    f.write("- Demonstrates practical relevance\n")
                elif 'Conclusion' in section['title']:
                    f.write("- Synthesizes main contributions\n")
                    f.write("- Discusses implications\n")
                    f.write("- Suggests future directions\n")
                else:
                    f.write("- Develops theoretical framework\n")
                    f.write("- Provides mathematical analysis\n")
                
                f.write("\n**Key Excerpts**:\n\n")
                for j, para in enumerate(key_paragraphs, 1):
                    # Truncate very long paragraphs
                    if len(para) > 500:
                        para = para[:500] + "..."
                    f.write(f"**Excerpt {j}**: \"{para}\"\n\n")
                
                f.write("**Analysis**: ")
                if 'Introduction' in section['title']:
                    f.write("Strong opening that establishes the mathematical problem context. ")
                    f.write("Notice the formal mathematical notation and precise definitions. ")
                    f.write("The introduction follows a clear progression from problem statement to solution approach.\n\n")
                elif 'Preliminaries' in section['title']:
                    f.write("Comprehensive background section that provides all necessary mathematical tools. ")
                    f.write("The notation is carefully established, which is crucial for a theoretical mathematics paper. ")
                    f.write("This section enables readers to follow the subsequent theoretical developments.\n\n")
                elif 'Characterization' in section['title'] or 'Tightness' in section['title']:
                    f.write("Core theoretical contribution of the paper. ")
                    f.write("The characterization provides necessary and sufficient conditions, which is a strong theoretical result. ")
                    f.write("The mathematical formalism is precise and rigorous.\n\n")
                else:
                    f.write("Well-structured section that contributes to the overall theoretical framework. ")
                    f.write("The mathematical development is clear and logically organized.\n\n")
            
            f.write("---\n\n")
        
        # Cross-disciplinary comparison
        f.write("## Cross-Disciplinary Comparison\n\n")
        f.write("### Mathematics vs. Applied Sciences\n\n")
        f.write("| Aspect | This Paper (Theoretical Math) | Applied Sciences |\n")
        f.write("|---|---|---|\n")
        f.write("| **Structure** | Definition-Theorem-Proof | Introduction-Methods-Results-Discussion |\n")
        f.write("| **Evidence** | Rigorous mathematical proofs | Empirical data and experiments |\n")
        f.write("| **Notation** | Highly formal mathematical notation | More accessible notation |\n")
        f.write("| **Contribution** | Theoretical characterization | Practical applications |\n")
        f.write("| **Evaluation** | Proof correctness and generality | Experimental validation |\n\n")
        
        # Key learning points
        f.write("## Key Learning Points for Imitation\n\n")
        f.write("1. **Mathematical Rigor**: Use of formal definitions and precise notation\n")
        f.write("2. **Theoretical Structure**: Clear progression from definitions to theorems to proofs\n")
        f.write("3. **Characterization Results**: Providing necessary and sufficient conditions\n")
        f.write("4. **Proof Techniques**: Systematic development of theoretical arguments\n")
        f.write("5. **Notation Consistency**: Careful establishment and consistent use of mathematical notation\n\n")
        
        # Imitation opportunities
        f.write("## Imitation Opportunities for Future Papers\n\n")
        f.write("### Structural Elements to Adapt\n")
        f.write("- **Definition-Theorem-Proof Structure**: Clear organization of theoretical content\n")
        f.write("- **Characterization Theorems**: Providing necessary and sufficient conditions\n")
        f.write("- **Systematic Notation**: Careful definition and consistent use of symbols\n")
        f.write("- **Proof Organization**: Logical flow from assumptions to conclusions\n\n")
        
        f.write("### Rhetorical Strategies\n")
        f.write("- **Problem Formulation**: Clear statement of mathematical problem\n")
        f.write("- **Theoretical Positioning**: Relating to existing mathematical literature\n")
        f.write("- **Rigorous Development**: Step-by-step theoretical argumentation\n")
        f.write("- **General Results**: Providing conditions that apply broadly\n\n")

def main():
    html_file = "paper_arxiv.html"
    md_output = "ZYJinInsights.md"
    
    print("Status: Starting analysis of HTML file...")
    print(f"Reading: {html_file}")
    
    paper_data = extract_sections(html_file)
    
    print(f"Status: Extracted {len(paper_data['sections'])} sections")
    print(f"Title: {paper_data['title']}")
    print(f"Authors: {', '.join(paper_data['authors'])}")
    
    print(f"Status: Generating markdown report...")
    generate_markdown_report(paper_data, md_output)
    
    print(f"Status: Report generated successfully: {md_output}")
    print(f"Total sections analyzed: {len(paper_data['sections'])}")
    print(f"Total paragraphs extracted: {sum(len(s['paragraphs']) for s in paper_data['sections'])}")

if __name__ == "__main__":
    main()
