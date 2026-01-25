#!/usr/bin/env python3
"""
Generate insights files for papers using LLM API
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

def read_paper_text(paper_dir):
    """Read extracted text from paper"""
    text_path = Path(paper_dir) / "paper_text.txt"
    if text_path.exists():
        with open(text_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def create_prompt(paper_text, arxiv_id):
    """Create prompt for LLM analysis"""
    # Read the instruction files
    base_dir = Path(__file__).parent.parent.parent
    sample_notes_path = base_dir / "writing" / "activity 1.2 analyze macro-level structure" / "sampleNotes.md"
    analyze_instructions_path = base_dir / "writing" / "activity 1.2 analyze macro-level structure" / "AnalyzePaper_1_AI.md"
    
    instructions = ""
    if analyze_instructions_path.exists():
        with open(analyze_instructions_path, 'r', encoding='utf-8') as f:
            instructions += f.read() + "\n\n"
    
    if sample_notes_path.exists():
        with open(sample_notes_path, 'r', encoding='utf-8') as f:
            instructions += "Reference framework:\n" + f.read()[:2000] + "\n\n"
    
    # Limit paper text to avoid token limits (use first ~30000 chars which is roughly 10-15 pages)
    paper_text_truncated = paper_text[:30000] if len(paper_text) > 30000 else paper_text
    
    prompt = f"""You are an expert academic writing instructor analyzing research papers for macro-level structure.

{instructions}

Now analyze the following paper (arXiv ID: {arxiv_id}):

{paper_text_truncated}

Create a comprehensive macro-level structure analysis following the format of KellerInsights.md. Include:
1. Paper metadata (title, authors, venue, field)
2. Overall macro-level assessment (structural framework, hourglass flow)
3. Section-by-section macro analysis with excerpts from the paper
4. Focus on CARS model for Introduction, literature review structure, methods, experiments
5. Include specific excerpts from the paper with section/page references
6. Analyze rhetorical moves, linguistic features, and discipline conventions

Generate the analysis in markdown format similar to writing/activity 1.2 analyze macro-level structure/KellerInsights.md"""
    
    return prompt

def call_poe_api(prompt, api_key):
    """Call Poe API to generate insights"""
    try:
        import openai
        
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.poe.com/v1"
        )
        
        print("   Calling Poe API (this may take 1-2 minutes)...")
        response = client.chat.completions.create(
            model="Assistant",  # Poe model name
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert academic writing instructor analyzing research papers for macro-level structure. Generate detailed, comprehensive analysis with specific excerpts from the paper."
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
        ("2405.19888", "ParrotInsights.md"),
        ("2312.07104", "SGLangInsights.md")
    ]
    
    for arxiv_id, output_name in papers:
        paper_dir = base_dir / arxiv_id
        print(f"\n=== Processing {arxiv_id} ===")
        
        # Read paper text
        paper_text = read_paper_text(paper_dir)
        if not paper_text:
            print(f"   Error: Could not read paper text from {paper_dir}/paper_text.txt")
            continue
        
        print(f"   Paper text loaded ({len(paper_text)} characters)")
        
        # Create prompt
        prompt = create_prompt(paper_text, arxiv_id)
        print(f"   Prompt created ({len(prompt)} characters)")
        
        # Call API
        insights = call_poe_api(prompt, api_key)
        if not insights:
            print(f"   Error: Failed to generate insights")
            continue
        
        # Save insights
        output_path = paper_dir / output_name
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(insights)
        
        print(f"   ✓ Insights saved to {output_path}")
        print(f"   Generated {len(insights)} characters")

if __name__ == "__main__":
    main()
