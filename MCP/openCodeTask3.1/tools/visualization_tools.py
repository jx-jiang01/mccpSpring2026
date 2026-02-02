"""HTML visualization generation tools"""

from pathlib import Path
from typing import Dict, Optional
import json


async def generate_hierarchical_html(
    structure: Dict, 
    output_path: Optional[str] = None,
    base_dir: Optional[Path] = None
) -> Dict:
    """Generate hierarchical HTML visualization"""
    
    if output_path is None:
        output_path = "visual.html"
    
    output_path = Path(output_path)
    
    # Load template
    if base_dir:
        template_path = base_dir / "templates" / "hierarchical.html"
    else:
        template_path = Path(__file__).parent.parent / "templates" / "hierarchical.html"
    
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
    else:
        # Fallback: generate basic HTML
        html_template = get_basic_hierarchical_template()
    
    # Generate HTML content
    html_content = generate_hierarchical_content(structure, html_template)
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return {
        "status": "success",
        "output_path": str(output_path),
        "file_size": len(html_content)
    }


async def generate_interconnected_html(
    structure: Dict,
    connections: Dict,
    output_path: Optional[str] = None,
    base_dir: Optional[Path] = None
) -> Dict:
    """Generate interconnected network HTML visualization"""
    
    if output_path is None:
        output_path = "visual_interconnection_text.html"
    
    output_path = Path(output_path)
    
    # Load template
    if base_dir:
        template_path = base_dir / "templates" / "interconnected.html"
    else:
        template_path = Path(__file__).parent.parent / "templates" / "interconnected.html"
    
    if template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
    else:
        # Fallback: generate basic HTML
        html_template = get_basic_interconnected_template()
    
    # Generate HTML content
    html_content = generate_interconnected_content(structure, connections, html_template)
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return {
        "status": "success",
        "output_path": str(output_path),
        "file_size": len(html_content)
    }


def generate_hierarchical_content(structure: Dict, template: str) -> str:
    """Generate hierarchical HTML content"""
    import html as html_module
    
    title = structure.get("title", "Paper Structure")
    author = structure.get("author", "")
    sections = structure.get("sections", [])
    
    # Escape HTML in title and author
    title = html_module.escape(str(title))
    author = html_module.escape(str(author))
    
    # Build sections HTML
    sections_html = ""
    for section in sections:
        heading = html_module.escape(str(section.get('heading', '')))
        excerpt = html_module.escape(str(section.get('text_excerpt', '')))
        level = section.get('level', 1)
        
        sections_html += f"""
        <div class="section level-{level}">
            <h{min(level, 6)} class="section-heading">{heading}</h{min(level, 6)}>
            <p class="section-excerpt">{excerpt}</p>
        """
        
        # Add subsections
        for subsection in section.get("subsections", []):
            sub_heading = html_module.escape(str(subsection.get('heading', '')))
            sub_excerpt = html_module.escape(str(subsection.get('text_excerpt', '')))
            sub_level = subsection.get('level', 2)
            
            sections_html += f"""
            <div class="subsection level-{sub_level}">
                <h{min(sub_level, 6)} class="subsection-heading">{sub_heading}</h{min(sub_level, 6)}>
                <p class="subsection-excerpt">{sub_excerpt}</p>
            </div>
            """
            
            # Add subsubsections
            for subsubsection in subsection.get("subsubsections", []):
                subsub_heading = html_module.escape(str(subsubsection.get('heading', '')))
                subsub_excerpt = html_module.escape(str(subsubsection.get('text_excerpt', '')))
                subsub_level = subsubsection.get('level', 3)
                
                sections_html += f"""
                <div class="subsubsection level-{subsub_level}">
                    <h{min(subsub_level, 6)} class="subsubsection-heading">{subsub_heading}</h{min(subsub_level, 6)}>
                    <p class="subsubsection-excerpt">{subsub_excerpt}</p>
                </div>
                """
        
        sections_html += "</div>"
    
    # Replace placeholders
    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{AUTHOR}}", author)
    html = html.replace("{{SECTIONS}}", sections_html)
    
    return html


def generate_interconnected_content(structure: Dict, connections: Dict, template: str) -> str:
    """Generate interconnected HTML content with network visualization"""
    import html as html_module
    import json
    
    title = structure.get("title", "Paper Structure")
    sections = structure.get("sections", [])
    connections_list = connections.get("connections", [])
    
    # Escape title for HTML
    title = html_module.escape(str(title))
    
    # Build sections data for JavaScript (escape for JSON)
    sections_data_list = []
    for i, section in enumerate(sections):
        sections_data_list.append({
            "id": i,
            "name": str(section.get("heading", "")),
            "text": str(section.get("text_excerpt", "")),
            "level": section.get("level", 1)
        })
    
    sections_data = json.dumps(sections_data_list, ensure_ascii=False)
    
    # Build connections data for JavaScript
    connections_data_list = []
    for conn in connections_list:
        connections_data_list.append({
            "source": str(conn.get("from", "")),
            "target": str(conn.get("to", "")),
            "type": str(conn.get("type", "unknown"))
        })
    
    connections_data = json.dumps(connections_data_list, ensure_ascii=False)
    
    # Replace placeholders
    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{SECTIONS_DATA}}", sections_data)
    html = html.replace("{{CONNECTIONS_DATA}}", connections_data)
    
    return html


def get_basic_hierarchical_template() -> str:
    """Fallback basic hierarchical template"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Structure: {{TITLE}}</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; }
        .container { max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }
        .section { margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #667eea; }
        .section-heading { color: #2d3748; margin-bottom: 10px; }
        .section-excerpt { color: #666; font-size: 0.9em; }
        .subsection { margin-left: 30px; margin-top: 10px; padding: 10px; background: #fff; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{TITLE}}</h1>
        <p><em>{{AUTHOR}}</em></p>
        {{SECTIONS}}
    </div>
</body>
</html>"""


def get_basic_interconnected_template() -> str:
    """Fallback basic interconnected template"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paper Structure: {{TITLE}}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #1a1a2e; color: #eee; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; text-align: center; }
        .main-container { display: flex; min-height: calc(100vh - 100px); }
        .network-panel { flex: 1; padding: 20px; }
        .detail-panel { width: 400px; background: #16213e; padding: 20px; border-left: 1px solid #333; }
        .section-node { padding: 10px; margin: 5px; background: #667eea; border-radius: 5px; cursor: pointer; }
        .section-node:hover { background: #764ba2; }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{TITLE}}</h1>
        <p>Interactive Network Visualization</p>
    </div>
    <div class="main-container">
        <div class="network-panel">
            <div id="network"></div>
        </div>
        <div class="detail-panel">
            <h3>Section Details</h3>
            <div id="details"></div>
        </div>
    </div>
    <script>
        const sections = {{SECTIONS_DATA}};
        const connections = {{CONNECTIONS_DATA}};
        // Network visualization code would go here
        document.getElementById('network').innerHTML = '<p>Network visualization (requires D3.js or similar library)</p>';
    </script>
</body>
</html>"""
