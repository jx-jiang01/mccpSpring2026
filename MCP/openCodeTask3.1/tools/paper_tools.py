"""Paper parsing and structure analysis tools"""

import re
import html
from pathlib import Path
from typing import Dict, List, Optional, Any


def extract_balanced_braces(text: str, start_pos: int) -> Optional[str]:
    """Extract content from balanced braces starting at start_pos"""
    if start_pos >= len(text) or text[start_pos] != '{':
        return None
    
    depth = 0
    i = start_pos
    start = start_pos + 1
    
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start:i]
        i += 1
    
    return None


def clean_latex_text(text: str) -> str:
    """Clean LaTeX commands and special characters for HTML display"""
    if not text:
        return ""
    
    # Remove LaTeX comments (lines starting with %)
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove inline comments but preserve the line if it has content before %
        if '%' in line:
            comment_pos = line.find('%')
            # Check if % is not part of a command or math
            if comment_pos > 0 and line[comment_pos-1] != '\\':
                line = line[:comment_pos]
        cleaned_lines.append(line)
    text = '\n'.join(cleaned_lines)
    
    # Convert citations to readable format
    text = re.sub(r'\\cite\{([^}]+)\}', r'[citation: \1]', text)
    text = re.sub(r'\\citep\{([^}]+)\}', r'[citation: \1]', text)
    text = re.sub(r'\\citet\{([^}]+)\}', r'[citation: \1]', text)
    
    # Convert references to readable format
    text = re.sub(r'\\ref\{([^}]+)\}', r'[ref: \1]', text)
    text = re.sub(r'\\eqref\{([^}]+)\}', r'[eq: \1]', text)
    
    # Remove label commands (not needed for display)
    text = re.sub(r'\\label\{[^}]+\}', '', text)
    
    # Convert math mode to readable format (inline)
    text = re.sub(r'\$([^$]+)\$', r'[\1]', text)
    # Convert display math
    text = re.sub(r'\\\[(.*?)\\\]', r'[\1]', text, flags=re.DOTALL)
    text = re.sub(r'\\\((.*?)\\\)', r'[\1]', text, flags=re.DOTALL)
    text = re.sub(r'\$\$(.*?)\$\$', r'[\1]', text, flags=re.DOTALL)
    
    # Remove footnote commands but keep content if possible
    text = re.sub(r'\\footnote\{([^}]+)\}', r' (note: \1)', text)
    text = re.sub(r'\\tnoteref\{[^}]+\}', '', text)
    text = re.sub(r'\\corref\{[^}]+\}', '', text)
    text = re.sub(r'\\fnref\{[^}]+\}', '', text)
    
    # Remove common LaTeX formatting commands (keep content)
    text = re.sub(r'\\textbf\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\textit\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\emph\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\texttt\{([^}]+)\}', r'\1', text)
    
    # Remove remaining LaTeX commands (simple ones without nested braces)
    # This handles commands like \section, \cite, etc. that we haven't caught
    text = re.sub(r'\\([a-zA-Z@]+)\*?\s*', '', text)
    
    # Clean up remaining braces (simple ones)
    # Be careful not to remove all braces - only simple {content} patterns
    text = re.sub(r'\{([^{}]+)\}', r'\1', text)
    
    # Remove LaTeX special characters that escaped
    text = re.sub(r'\\[^\w\s]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # Escape HTML special characters (do this last)
    text = html.escape(text)
    
    return text


def extract_latex_title(content: str) -> str:
    """Extract title from LaTeX, handling nested braces"""
    # Try to find \title{...}
    title_match = re.search(r'\\title\s*\{', content)
    if not title_match:
        return "Untitled Paper"
    
    start_pos = title_match.end() - 1  # Position of opening brace
    title = extract_balanced_braces(content, start_pos)
    
    if title:
        # Clean LaTeX commands from title
        title = clean_latex_text(title)
        # Remove footnote references
        title = re.sub(r'\\tnoteref\{[^}]+\}', '', title)
        title = re.sub(r'\\footnote\{[^}]+\}', '', title)
        return title.strip() or "Untitled Paper"
    
    return "Untitled Paper"


def extract_latex_author(content: str) -> str:
    """Extract author from LaTeX, handling nested braces"""
    # Try to find \author{...}
    author_match = re.search(r'\\author\s*\{', content)
    if not author_match:
        return "Unknown"
    
    start_pos = author_match.end() - 1  # Position of opening brace
    author = extract_balanced_braces(content, start_pos)
    
    if author:
        # Clean LaTeX commands from author
        author = clean_latex_text(author)
        # Remove footnote references
        author = re.sub(r'\\corref\{[^}]+\}', '', author)
        author = re.sub(r'\\fnref\{[^}]+\}', '', author)
        return author.strip() or "Unknown"
    
    return "Unknown"


async def parse_paper_structure(file_path: Optional[str] = None, file_content: Optional[str] = None) -> Dict:
    """Parse paper structure from LaTeX, PDF, or Markdown"""
    
    if file_content:
        content = file_content
        source = "provided_content"
    elif file_path:
        file_path_obj = Path(file_path).expanduser().resolve()
        if not file_path_obj.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path_obj, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        source = str(file_path_obj)
    else:
        raise ValueError("Either file_path or file_content must be provided")
    
    # Detect format and parse accordingly
    if file_path:
        file_ext = Path(file_path).suffix.lower()
        if file_ext == '.tex':
            return parse_latex_structure(content, source)
        elif file_ext in ['.html', '.htm']:
            return parse_html_structure(content, source)
        elif file_ext in ['.md', '.markdown']:
            return parse_markdown_structure(content, source)
    
    # Try LaTeX parsing by default
    return parse_latex_structure(content, source)


def parse_latex_structure(content: str, source: str) -> Dict:
    """Parse LaTeX document structure"""
    
    # Extract title (handling nested braces)
    title = extract_latex_title(content)
    
    # Extract author (handling nested braces)
    author = extract_latex_author(content)
    
    # Extract sections
    sections = []
    
    # Pattern for sections: \section{...}, \subsection{...}, etc.
    section_pattern = r'\\(section|subsection|subsubsection|paragraph)\{([^}]+)\}'
    
    current_section = None
    current_subsection = None
    current_subsubsection = None
    
    for match in re.finditer(section_pattern, content):
        level_type = match.group(1)
        heading = match.group(2)
        position = match.start()
        
        # Clean heading (remove LaTeX commands)
        heading = clean_latex_text(heading)
        
        # Get text excerpt (next 400 chars after heading, then clean)
        excerpt_start = match.end()
        excerpt_end = min(excerpt_start + 400, len(content))
        raw_excerpt = content[excerpt_start:excerpt_end]
        
        # Clean the excerpt (removes LaTeX commands, comments, etc.)
        text_excerpt = clean_latex_text(raw_excerpt)
        text_excerpt = text_excerpt[:200] + "..." if len(text_excerpt) > 200 else text_excerpt
        
        section_data = {
            "level": get_section_level(level_type),
            "heading": heading,
            "text_excerpt": text_excerpt,
            "position": position
        }
        
        if level_type == 'section':
            current_section = {
                **section_data,
                "subsections": []
            }
            sections.append(current_section)
            current_subsection = None
            current_subsubsection = None
        
        elif level_type == 'subsection' and current_section:
            current_subsection = {
                **section_data,
                "subsubsections": []
            }
            current_section["subsections"].append(current_subsection)
            current_subsubsection = None
        
        elif level_type == 'subsubsection' and current_subsection:
            current_subsubsection = section_data
            current_subsection["subsubsections"].append(current_subsubsection)
    
    # Extract abstract if present
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
    abstract = abstract_match.group(1).strip() if abstract_match else None
    
    return {
        "status": "success",
        "source": source,
        "title": title,
        "author": author,
        "abstract": abstract,
        "sections": sections,
        "section_count": len(sections)
    }


def parse_markdown_structure(content: str, source: str) -> Dict:
    """Parse Markdown document structure"""
    
    lines = content.split('\n')
    title = "Untitled Paper"
    sections = []
    
    current_section = None
    
    for i, line in enumerate(lines):
        # Extract title (first # heading)
        if line.startswith('# ') and not title or title == "Untitled Paper":
            title = line[2:].strip()
            continue
        
        # Match headings
        heading_match = re.match(r'^(#{1,4})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            heading = heading_match.group(2).strip()
            
            # Get text excerpt (next few lines)
            excerpt_lines = []
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('#'):
                    excerpt_lines.append(lines[j].strip())
            text_excerpt = ' '.join(excerpt_lines[:3])
            
            section_data = {
                "level": level,
                "heading": heading,
                "text_excerpt": text_excerpt[:150] + "..." if len(text_excerpt) > 150 else text_excerpt,
                "position": i
            }
            
            if level == 1:
                current_section = {
                    **section_data,
                    "subsections": []
                }
                sections.append(current_section)
            elif level == 2 and current_section:
                current_section["subsections"].append(section_data)
    
    return {
        "status": "success",
        "source": source,
        "title": title,
        "sections": sections,
        "section_count": len(sections)
    }


def parse_html_structure(content: str, source: str) -> Dict:
    """Parse HTML document structure"""
    
    # Extract title
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Untitled Paper"
    
    # Extract h1-h6 headings
    sections = []
    current_section = None
    
    # Pattern for headings: <h1>...</h1>, <h2>...</h2>, etc.
    heading_pattern = r'<h([1-6])[^>]*>(.*?)</h[1-6]>'
    
    for match in re.finditer(heading_pattern, content, re.IGNORECASE | re.DOTALL):
        level = int(match.group(1))
        heading_text = html.unescape(re.sub(r'<[^>]+>', '', match.group(2))).strip()
        
        if not heading_text:
            continue
        
        # Get text excerpt (next 200 chars after heading)
        excerpt_start = match.end()
        excerpt_end = min(excerpt_start + 200, len(content))
        text_excerpt = content[excerpt_start:excerpt_end]
        # Remove HTML tags from excerpt
        text_excerpt = re.sub(r'<[^>]+>', '', text_excerpt).strip()
        text_excerpt = html.unescape(text_excerpt)
        text_excerpt = re.sub(r'\s+', ' ', text_excerpt)
        
        section_data = {
            "level": level,
            "heading": heading_text,
            "text_excerpt": text_excerpt[:150] + "..." if len(text_excerpt) > 150 else text_excerpt,
            "position": match.start()
        }
        
        if level == 1:
            current_section = {
                **section_data,
                "subsections": []
            }
            sections.append(current_section)
        elif level == 2 and current_section:
            current_section["subsections"].append(section_data)
        elif level >= 3 and current_section and current_section.get("subsections"):
            # Add to last subsection
            if current_section["subsections"]:
                current_section["subsections"][-1].setdefault("subsubsections", []).append(section_data)
    
    return {
        "status": "success",
        "source": source,
        "title": title,
        "sections": sections,
        "section_count": len(sections)
    }


def get_section_level(level_type: str) -> int:
    """Convert LaTeX section type to numeric level"""
    level_map = {
        'section': 1,
        'subsection': 2,
        'subsubsection': 3,
        'paragraph': 4
    }
    return level_map.get(level_type, 1)


async def analyze_section_interconnections(structure: Dict, file_path: Optional[str] = None) -> Dict:
    """Analyze relationships between sections"""
    
    sections = structure.get("sections", [])
    connections = []
    
    if not sections:
        return {
            "status": "success",
            "sections": sections,
            "connections": connections,
            "connection_count": 0
        }
    
    # Build section index
    section_index = {}
    for i, section in enumerate(sections):
        section_index[section["heading"]] = {
            "index": i,
            "section": section
        }
        for j, subsection in enumerate(section.get("subsections", [])):
            section_index[subsection["heading"]] = {
                "index": (i, j),
                "section": subsection,
                "parent": section["heading"]
            }
    
    # Analyze connections
    for i, section in enumerate(sections):
        # 1. Sequential connection to next section (always add)
        if i < len(sections) - 1:
            connections.append({
                "from": section["heading"],
                "to": sections[i + 1]["heading"],
                "type": "sequential",
                "strength": "strong"
            })
        
        # 2. Hierarchical connections (section to subsections)
        for subsection in section.get("subsections", []):
            connections.append({
                "from": section["heading"],
                "to": subsection["heading"],
                "type": "hierarchical",
                "strength": "strong"
            })
            
            # Subsection to subsubsections
            for subsubsection in subsection.get("subsubsections", []):
                connections.append({
                    "from": subsection["heading"],
                    "to": subsubsection["heading"],
                    "type": "hierarchical",
                    "strength": "strong"
                })
        
        # 3. Semantic connections based on keywords
        text = section.get("text_excerpt", "").lower()
        heading_lower = section["heading"].lower()
        
        # Introduction typically connects to Methods/Approach
        if "introduction" in heading_lower:
            for other_section in sections:
                other_heading = other_section["heading"].lower()
                if any(keyword in other_heading for keyword in ["method", "approach", "algorithm", "proposed"]):
                    connections.append({
                        "from": section["heading"],
                        "to": other_section["heading"],
                        "type": "semantic",
                        "strength": "medium"
                    })
        
        # Methods/Approach connects to Results/Experiments
        if any(keyword in heading_lower for keyword in ["method", "approach", "algorithm", "proposed"]):
            for other_section in sections:
                other_heading = other_section["heading"].lower()
                if any(keyword in other_heading for keyword in ["result", "experiment", "evaluation", "performance"]):
                    connections.append({
                        "from": section["heading"],
                        "to": other_section["heading"],
                        "type": "semantic",
                        "strength": "medium"
                    })
        
        # Results connects to Discussion/Conclusion
        if any(keyword in heading_lower for keyword in ["result", "experiment", "evaluation"]):
            for other_section in sections:
                other_heading = other_section["heading"].lower()
                if any(keyword in other_heading for keyword in ["discussion", "conclusion", "future"]):
                    connections.append({
                        "from": section["heading"],
                        "to": other_section["heading"],
                        "type": "semantic",
                        "strength": "medium"
                    })
        
        # Related work connects to Introduction and Methods
        if any(keyword in heading_lower for keyword in ["related", "previous", "literature"]):
            for other_section in sections:
                other_heading = other_section["heading"].lower()
                if "introduction" in other_heading or any(kw in other_heading for kw in ["method", "approach"]):
                    connections.append({
                        "from": section["heading"],
                        "to": other_section["heading"],
                        "type": "semantic",
                        "strength": "weak"
                    })
    
    # Remove duplicate connections
    seen = set()
    unique_connections = []
    for conn in connections:
        conn_key = (conn["from"], conn["to"], conn["type"])
        if conn_key not in seen:
            seen.add(conn_key)
            unique_connections.append(conn)
    
    return {
        "status": "success",
        "sections": sections,
        "connections": unique_connections,
        "connection_count": len(unique_connections)
    }
