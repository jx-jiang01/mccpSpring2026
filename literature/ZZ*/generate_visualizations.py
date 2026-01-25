#!/usr/bin/env python3
"""
Generate visualization HTML files for papers using LLM API
"""

import os
import sys
from pathlib import Path

def load_api_key():
    """Load Poe API key"""
    key_path = Path(__file__).parent.parent.parent / "LLM" / "poe.md"
    if key_path.exists():
        with open(key_path, 'r') as f:
            return f.read().strip().split('\n')[0]
    return None

def read_insights(insights_path):
    """Read insights markdown file"""
    if insights_path.exists():
        with open(insights_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def create_html_prompt(insights_content, paper_title, arxiv_id):
    """Create prompt for HTML visualization generation"""
    # Read the example visualization
    base_dir = Path(__file__).parent.parent.parent
    example_html_path = base_dir / "writing" / "activity 1.2 analyze macro-level structure" / "visualSample.html"
    
    example_html = ""
    if example_html_path.exists():
        with open(example_html_path, 'r', encoding='utf-8') as f:
            example_html = f.read()[:5000]  # Use first 5000 chars as template reference
    
    prompt = f"""Generate a visualization HTML file for the paper analysis provided below. Use the visualSample.html format from writing/activity 1.2 analyze macro-level structure as a template.

Paper: {paper_title} (arXiv: {arxiv_id})

Analysis Content:
{insights_content[:15000]}  # Limit to avoid token limits

Generate a complete HTML file with:
1. HTML structure with CSS styling (similar to visualSample.html)
2. Visual representation of the macro-level structure
3. Sections with color-coded moves (Introduction, Related Work, Methods, Experiments, etc.)
4. Key excerpts from the paper
5. Analysis annotations
6. Responsive design

The HTML should be a complete, self-contained file that can be opened directly in a browser. Use the same styling approach as visualSample.html but adapt it for this specific paper's structure."""
    
    return prompt

def call_poe_api(prompt, api_key):
    """Call Poe API to generate HTML"""
    try:
        import openai
        
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.poe.com/v1"
        )
        
        print("   Calling Poe API for HTML generation (this may take 1-2 minutes)...")
        response = client.chat.completions.create(
            model="Assistant",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert web developer and academic writing instructor. Generate complete, well-formatted HTML files for visualizing paper structure."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=4000
        )
        
        return response.choices[0].message.content
        
    except ImportError:
        print("   Error: openai package not installed. Run: pip install openai")
        return None
    except Exception as e:
        print(f"   Error calling API: {e}")
        return None

def clean_html_content(content):
    """Clean HTML content if wrapped in markdown code blocks"""
    if content.startswith('```html'):
        lines = content.split('\n')
        if lines[-1].strip() == '```':
            return '\n'.join(lines[1:-1])
    elif '```html' in content:
        start = content.find('```html') + len('```html')
        end = content.rfind('```')
        if end > start:
            return content[start:end].strip()
    return content

def main():
    """Main function"""
    base_dir = Path(__file__).parent
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        print("Error: Poe API key not found in LLM/poe.md")
        return
    
    # Process each paper
    papers = [
        ("2405.19888", "ParrotInsights.md", "ParrotInsightsVisualization.html", "Parrot: Efficient Serving of LLM-based Applications with Semantic Variable"),
        ("2312.07104", "SGLangInsights.md", "SGLangVisualization.html", "SGLang: Efficient Execution of Structured Language Model Programs")
    ]
    
    for arxiv_id, insights_file, output_html, paper_title in papers:
        paper_dir = base_dir / arxiv_id
        print(f"\n=== Generating visualization for {arxiv_id} ===")
        
        # Read insights
        insights_path = paper_dir / insights_file
        insights_content = read_insights(insights_path)
        if not insights_content:
            print(f"   Error: Could not read insights from {insights_path}")
            continue
        
        print(f"   Insights loaded ({len(insights_content)} characters)")
        
        # Create prompt
        prompt = create_html_prompt(insights_content, paper_title, arxiv_id)
        print(f"   Prompt created ({len(prompt)} characters)")
        
        # Call API
        html_content = call_poe_api(prompt, api_key)
        if not html_content:
            print(f"   Error: Failed to generate HTML")
            continue
        
        # Clean HTML
        html_content = clean_html_content(html_content)
        
        # Save HTML
        output_path = paper_dir / output_html
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"   ✓ Visualization saved to {output_path}")
        print(f"   Generated {len(html_content)} characters")

if __name__ == "__main__":
    main()
