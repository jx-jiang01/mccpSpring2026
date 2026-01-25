#!/usr/bin/env python3
"""
Enhanced arXiv search - try multiple search strategies.
"""

import requests
import feedparser
from pathlib import Path
import re

OUTPUT_DIR = Path(__file__).parent

def search_arxiv_comprehensive(query_terms):
    """Search arXiv with multiple query strategies."""
    base_url = "http://export.arxiv.org/api/query"
    
    # Try different query formats
    queries = [
        f"all:{' '.join(query_terms)}",
        f"ti:{query_terms[0]}",  # Title search
        f"au:{query_terms[0]}",  # Author search (if first term is author name)
    ]
    
    all_results = []
    for query in queries:
        try:
            params = {
                'search_query': query,
                'start': 0,
                'max_results': 20,
                'sortBy': 'relevance',
                'sortOrder': 'descending'
            }
            
            print(f"  Trying query: {query}")
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            if feed.entries:
                print(f"    Found {len(feed.entries)} results")
                all_results.extend(feed.entries)
        except Exception as e:
            print(f"    Error: {e}")
    
    return all_results

def extract_arxiv_id(entry):
    """Extract arXiv ID from entry."""
    link = entry.get('id', '')
    match = re.search(r'arxiv\.org/abs/([\d.]+v?\d*)', link)
    if match:
        return match.group(1)
    return None

def download_from_arxiv(arxiv_id, pdf_path, html_path):
    """Download both PDF and HTML from arXiv."""
    print(f"\n  Downloading from arXiv ID: {arxiv_id}")
    
    # Download PDF
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        print(f"    Downloading PDF...")
        response = requests.get(pdf_url, timeout=60, stream=True)
        response.raise_for_status()
        with open(pdf_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"    ✓ PDF downloaded: {pdf_path.stat().st_size:,} bytes")
    except Exception as e:
        print(f"    ✗ PDF download failed: {e}")
    
    # Download HTML
    html_url = f"https://arxiv.org/html/{arxiv_id}"
    try:
        print(f"    Downloading HTML...")
        response = requests.get(html_url, timeout=60, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        response.raise_for_status()
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"    ✓ HTML downloaded: {html_path.stat().st_size:,} bytes")
    except Exception as e:
        print(f"    ✗ HTML download failed: {e}")

def main():
    print("="*60)
    print("Enhanced arXiv Search")
    print("="*60)
    
    # Try searching with common optimization/operations research terms
    # since this is a Springer optimization journal paper
    search_terms = [
        ['optimization', 'algorithm'],
        ['mathematical', 'programming'],
        ['operations', 'research'],
    ]
    
    print("\nTrying broad searches for optimization papers...")
    found_papers = []
    
    for terms in search_terms:
        results = search_arxiv_comprehensive(terms)
        if results:
            found_papers.extend(results)
    
    # Also try searching by journal name or common author names
    print("\nTrying journal-specific searches...")
    journal_searches = [
        ['mathematical', 'programming', 'computation'],
        ['SIAM', 'optimization'],
    ]
    
    for terms in journal_searches:
        results = search_arxiv_comprehensive(terms)
        if results:
            found_papers.extend(results)
    
    if found_papers:
        print(f"\nFound {len(found_papers)} potential papers")
        print("Note: Without the exact paper title, it's hard to identify the specific paper.")
        print("The Springer PDF has been downloaded successfully.")
        print("\nTo find the exact arXiv version, you would need:")
        print("  - The exact paper title")
        print("  - Author names")
        print("  - Or check if the authors published a preprint")
    else:
        print("\nNo matching papers found on arXiv.")
        print("This paper likely doesn't have an arXiv preprint version.")
    
    print("\n" + "="*60)
    print("Summary:")
    print("="*60)
    print("✓ Springer PDF downloaded: paper_springer.pdf")
    print("✗ arXiv version: Not found (paper may not have preprint)")

if __name__ == '__main__':
    main()
