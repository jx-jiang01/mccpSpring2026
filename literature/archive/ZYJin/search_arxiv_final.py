#!/usr/bin/env python3
"""
Search arXiv for the specific paper and download PDF and HTML.
"""

import requests
import feedparser
from pathlib import Path
import re

# Paper information extracted from PDF
PAPER = {
    'title': 'A characterization for tightness of the sparse Moment-SOS hierarchy',
    'authors': ['Jiawang Nie', 'Zheng Qu', 'Xindong Tang', 'Linghao Zhang'],
    'keywords': ['Moment-SOS', 'sparse', 'polynomial optimization', 'tightness'],
    'pdf_filename': 'paper_arxiv.pdf',
    'html_filename': 'paper_arxiv.html'
}

OUTPUT_DIR = Path(__file__).parent

def search_arxiv(query, max_results=20):
    """Search arXiv using the API."""
    url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'relevance',
        'sortOrder': 'descending'
    }
    
    print(f"  Searching: {query}")
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    
    feed = feedparser.parse(response.content)
    return feed.entries

def extract_arxiv_id(entry):
    """Extract arXiv ID from entry."""
    link = entry.get('id', '')
    match = re.search(r'arxiv\.org/abs/([\d.]+v?\d*)', link)
    if match:
        return match.group(1)
    return None

def find_matching_paper(entries):
    """Find the paper that matches our criteria."""
    for entry in entries:
        title = entry.get('title', '').lower()
        authors = [a.get('name', '') for a in entry.get('authors', [])]
        author_names = ' '.join(authors).lower()
        
        # Check for key terms in title
        title_match = any(kw.lower() in title for kw in ['moment-sos', 'sparse', 'tightness', 'hierarchy'])
        
        # Check for author match
        author_match = any(auth.lower() in author_names for auth in PAPER['authors'])
        
        if title_match or author_match:
            print(f"\n  Potential match found:")
            print(f"    Title: {entry.get('title', 'N/A')}")
            print(f"    Authors: {', '.join(authors)}")
            print(f"    Published: {entry.get('published', 'N/A')}")
            
            arxiv_id = extract_arxiv_id(entry)
            if arxiv_id:
                print(f"    arXiv ID: {arxiv_id}")
                return arxiv_id, entry
    
    return None, None

def download_arxiv_pdf(arxiv_id, output_path):
    """Download PDF from arXiv."""
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    
    print(f"\n  Downloading PDF from: {pdf_url}")
    response = requests.get(pdf_url, timeout=60, stream=True)
    response.raise_for_status()
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    
    file_size = output_path.stat().st_size
    print(f"  ✓ PDF downloaded: {output_path.name} ({file_size:,} bytes)")
    return True

def download_arxiv_html(arxiv_id, output_path):
    """Download HTML version from arXiv."""
    html_url = f"https://arxiv.org/html/{arxiv_id}"
    
    print(f"  Downloading HTML from: {html_url}")
    response = requests.get(html_url, timeout=60, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    response.raise_for_status()
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    file_size = output_path.stat().st_size
    print(f"  ✓ HTML downloaded: {output_path.name} ({file_size:,} bytes)")
    return True

def main():
    print("="*60)
    print("arXiv Search for: A characterization for tightness of the sparse Moment-SOS hierarchy")
    print("="*60)
    print(f"Authors: {', '.join(PAPER['authors'])}")
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    # Try multiple search queries
    queries = [
        f"ti:\"Moment-SOS hierarchy\"",
        f"ti:\"sparse Moment-SOS\"",
        f"all:Moment-SOS sparse tightness",
        f"au:\"Jiawang Nie\"",
        f"au:\"Zheng Qu\"",
        f"all:polynomial optimization sparse hierarchy",
    ]
    
    arxiv_id = None
    matching_entry = None
    
    for query in queries:
        try:
            entries = search_arxiv(query, max_results=10)
            if entries:
                print(f"    Found {len(entries)} results")
                arxiv_id, matching_entry = find_matching_paper(entries)
                if arxiv_id:
                    break
        except Exception as e:
            print(f"    Error: {e}")
            continue
    
    if arxiv_id:
        print(f"\n{'='*60}")
        print("Downloading from arXiv...")
        print(f"{'='*60}")
        
        pdf_path = OUTPUT_DIR / PAPER['pdf_filename']
        html_path = OUTPUT_DIR / PAPER['html_filename']
        
        try:
            download_arxiv_pdf(arxiv_id, pdf_path)
        except Exception as e:
            print(f"  ✗ PDF download failed: {e}")
        
        try:
            download_arxiv_html(arxiv_id, html_path)
        except Exception as e:
            print(f"  ✗ HTML download failed: {e}")
        
        print(f"\n✓ Successfully downloaded from arXiv!")
    else:
        print(f"\n{'='*60}")
        print("Result: Paper not found on arXiv")
        print(f"{'='*60}")
        print("\nThis paper may not have an arXiv preprint version.")
        print("The Springer PDF has been downloaded: paper_springer.pdf")

if __name__ == '__main__':
    main()
