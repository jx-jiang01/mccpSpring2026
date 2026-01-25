#!/usr/bin/env python3
"""
Script to generate HTML visualization of the paper structure analysis.
"""

import json
from analyze_paper import extract_sections

def generate_html_visualization(paper_data, output_file):
    """Generate HTML visualization similar to visualSample.html."""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{paper_data['title']} Macro-Level Structure Visualization</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }}
        .structure-diagram {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .section {{
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 15px;
            background: #ecf0f1;
            position: relative;
        }}
        .section-header {{
            background: #3498db;
            color: white;
            padding: 10px;
            margin: -15px -15px 15px -15px;
            border-radius: 6px 6px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .section-title {{
            font-weight: bold;
            font-size: 1.2em;
        }}
        .word-count {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        .moves {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }}
        .move {{
            background: white;
            padding: 10px;
            border-radius: 5px;
            border-left: 4px solid #e74c3c;
        }}
        .move-title {{
            font-weight: bold;
            color: #e74c3c;
            margin-bottom: 5px;
        }}
        .move-content {{
            font-size: 0.9em;
            color: #555;
        }}
        .key-excerpt {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            font-style: italic;
            font-size: 0.9em;
        }}
        .analysis {{
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            font-size: 0.9em;
        }}
        .flow-arrow {{
            text-align: center;
            font-size: 2em;
            color: #7f8c8d;
            margin: 10px 0;
        }}
        .comparison-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }}
        .comparison-table th, .comparison-table td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        .comparison-table th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .highlight {{
            background-color: #fff3cd;
            font-weight: bold;
        }}
        .legend {{
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .legend-item {{
            display: inline-block;
            margin: 5px 15px 5px 0;
            padding: 5px 10px;
            border-radius: 3px;
            font-size: 0.9em;
        }}
        .math-convention {{ background: #3498db; color: white; }}
        .applied {{ background: #e74c3c; color: white; }}
        .universal {{ background: #27ae60; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{paper_data['title']}: Macro-Level Structure Analysis</h1>
        
        <div class="legend">
            <h3>Analysis Framework</h3>
            <div class="legend-item math-convention">Theoretical Mathematics Convention</div>
            <div class="legend-item applied">Applied Sciences</div>
            <div class="legend-item universal">Universal Best Practice</div>
        </div>

        <div class="structure-diagram">
"""
    
    # Add sections
    for i, section in enumerate(paper_data['sections']):
        para_count = len(section['paragraphs'])
        section_num = section['title'].split('.')[0] if '.' in section['title'] else str(i+1)
        
        # Determine section type for analysis
        section_type = "Theoretical Development"
        if 'Introduction' in section['title']:
            section_type = "Problem Formulation"
        elif 'Preliminaries' in section['title']:
            section_type = "Mathematical Background"
        elif 'Characterization' in section['title'] or 'Tightness' in section['title']:
            section_type = "Main Results"
        elif 'Proof' in section['title']:
            section_type = "Rigorous Proofs"
        elif 'Example' in section['title']:
            section_type = "Concrete Applications"
        elif 'Conclusion' in section['title']:
            section_type = "Synthesis & Future Work"
        
        # Get key excerpt (first paragraph, cleaned)
        key_excerpt = ""
        if section['paragraphs']:
            excerpt = section['paragraphs'][0]
            # Clean up LaTeX artifacts
            excerpt = excerpt[:300] + "..." if len(excerpt) > 300 else excerpt
            key_excerpt = excerpt
        
        html_content += f"""
            <!-- Section {i+1} -->
            <div class="section">
                <div class="section-header">
                    <span class="section-title">Section {section_num}: {section['title'].split('.', 1)[-1].strip() if '.' in section['title'] else section['title']}</span>
                    <span class="word-count">~{para_count} paragraphs</span>
                </div>

                <div class="moves">
                    <div class="move">
                        <div class="move-title">Section Type: {section_type}</div>
                        <div class="move-content">
                            <strong>Content:</strong> {section_type.lower()} with {para_count} paragraphs
                        </div>
"""
        
        if key_excerpt:
            html_content += f"""
                        <div class="key-excerpt">
                            "{key_excerpt}"
                        </div>
"""
        
        # Add analysis based on section type
        analysis_text = ""
        if 'Introduction' in section['title']:
            analysis_text = "Strong opening that establishes mathematical problem context with formal notation and precise definitions."
        elif 'Preliminaries' in section['title']:
            analysis_text = "Comprehensive background providing necessary mathematical tools and establishing consistent notation."
        elif 'Characterization' in section['title'] or 'Tightness' in section['title']:
            analysis_text = "Core theoretical contribution providing necessary and sufficient conditions with rigorous mathematical formalism."
        elif 'Proof' in section['title']:
            analysis_text = "Rigorous mathematical proofs demonstrating theoretical validity using standard proof techniques."
        elif 'Example' in section['title']:
            analysis_text = "Concrete examples illustrating theoretical concepts and demonstrating practical relevance."
        elif 'Conclusion' in section['title']:
            analysis_text = "Synthesis of main contributions with discussion of implications and future directions."
        else:
            analysis_text = "Well-structured theoretical development contributing to the overall mathematical framework."
        
        html_content += f"""
                        <div class="analysis">
                            {analysis_text}
                        </div>
                    </div>
                </div>
            </div>
"""
        
        # Add flow arrow between sections (except after last section)
        if i < len(paper_data['sections']) - 1:
            html_content += """
            <div class="flow-arrow">↓</div>
"""
    
    # Add comparison table
    html_content += """
        </div>

        <h2>Cross-Disciplinary Comparison</h2>
        <table class="comparison-table">
            <tr>
                <th>Aspect</th>
                <th>This Paper (Theoretical Math)</th>
                <th>Applied Sciences</th>
                <th>Key Learning</th>
            </tr>
            <tr>
                <td>Structure</td>
                <td class="highlight">Definition-Theorem-Proof</td>
                <td>Introduction-Methods-Results-Discussion</td>
                <td>Theoretical math emphasizes logical proof structure</td>
            </tr>
            <tr>
                <td>Evidence</td>
                <td class="highlight">Rigorous mathematical proofs</td>
                <td>Empirical data and experiments</td>
                <td>Mathematical validity through proof, not experimentation</td>
            </tr>
            <tr>
                <td>Notation</td>
                <td class="highlight">Highly formal mathematical notation</td>
                <td>More accessible notation</td>
                <td>Precise mathematical formalism is essential</td>
            </tr>
            <tr>
                <td>Contribution</td>
                <td class="highlight">Theoretical characterization</td>
                <td>Practical applications</td>
                <td>Mathematical papers emphasize theoretical generality</td>
            </tr>
            <tr>
                <td>Evaluation</td>
                <td class="highlight">Proof correctness and generality</td>
                <td>Experimental validation</td>
                <td>Mathematical rigor through logical argumentation</td>
            </tr>
        </table>

        <h2>Imitation Framework for Future Papers</h2>
        <div class="analysis">
            <h3>Structural Elements to Adapt:</h3>
            <ul>
                <li><strong>Definition-Theorem-Proof Structure:</strong> Clear organization of theoretical content</li>
                <li><strong>Characterization Theorems:</strong> Providing necessary and sufficient conditions</li>
                <li><strong>Systematic Notation:</strong> Careful definition and consistent use of mathematical symbols</li>
                <li><strong>Proof Organization:</strong> Logical flow from assumptions to conclusions</li>
            </ul>

            <h3>Rhetorical Strategies:</h3>
            <ul>
                <li><strong>Problem Formulation:</strong> Clear statement of mathematical problem</li>
                <li><strong>Theoretical Positioning:</strong> Relating to existing mathematical literature</li>
                <li><strong>Rigorous Development:</strong> Step-by-step theoretical argumentation</li>
                <li><strong>General Results:</strong> Providing conditions that apply broadly</li>
            </ul>

            <h3>Quality Indicators:</h3>
            <ul>
                <li><strong>Mathematical Rigor:</strong> Formal definitions and precise notation</li>
                <li><strong>Theoretical Validity:</strong> Correct and complete proofs</li>
                <li><strong>Notation Consistency:</strong> Careful establishment and consistent use</li>
                <li><strong>Generality:</strong> Results applicable to broad classes of problems</li>
            </ul>
        </div>

        <div style="text-align: center; margin-top: 30px; color: #7f8c8d; font-size: 0.9em;">
            <p>Analysis based on macro-level structure framework from academic writing pedagogy</p>
            <p>Interactive visualization for learning paper organization patterns</p>
        </div>
    </div>
</body>
</html>
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    html_file = "paper_arxiv.html"
    html_output = "visualSample.html"
    
    print("Status: Generating HTML visualization...")
    print(f"Reading: {html_file}")
    
    paper_data = extract_sections(html_file)
    
    print(f"Status: Generating HTML visualization...")
    generate_html_visualization(paper_data, html_output)
    
    print(f"Status: HTML visualization generated successfully: {html_output}")

if __name__ == "__main__":
    main()
