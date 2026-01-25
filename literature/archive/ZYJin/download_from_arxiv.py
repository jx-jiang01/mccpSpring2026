#!/usr/bin/env python3
"""
Search arXiv for paper and download both PDF and HTML versions.
"""

import requests
import feedparser
from pathlib import Path
import time
import re

# Paper information
PAPER = {
    'doi': '10.1007/s10107-025-02223-2',
    'springer_url': 'https://link.springer.com/content/pdf/10.1007/s10107-025-02223-2.pdf',
    'pdf_filename': 'paper_arxiv.pdf',
    'html_filename': 'paper_arxiv.html'
}

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

def search_arxiv_by_doi(doi):
    """Search arXiv using DOI."""
    # Remove the prefix to get the numeric part
    doi_part = doi.replace('10.1007/', '').replace('10.1145/', '')
    
    # Try searching with DOI
    queries = [
        f'arXiv:{doi_part}',
        f'doi:{doi}',
        doi_part,
    ]
    
    for query in queries:
        try:
            url = "http://export.arxiv.org/api/query"
            params = {
                'search_query': query,
                'start': 0,
                'max_results': 10,
                'sortBy': 'relevance',
                'sortOrder': 'descending'
            }
            
            print(f"  Searching arXiv with query: {query}")
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            if feed.entries:
                return feed.entries
        except Exception as e:
            print(f"  ⚠ Error with query '{query}': {e}")
            continue
    
    return []

def search_arxiv_by_keywords(keywords):
    """Search arXiv using keywords."""
    query = ' '.join(keywords)
    url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': 20,
        'sortBy': 'relevance',
        'sortOrder': 'descending'
    }
    
    print(f"  Searching arXiv with keywords: {query}")
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

def download_arxiv_pdf(arxiv_id, output_path):
    """Download PDF from arXiv."""
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    
    print(f"  Downloading PDF from: {pdf_url}")
    response = requests.get(pdf_url, timeout=60, stream=True)
    response.raise_for_status()
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    
    file_size = output_path.stat().st_size
    print(f"  ✓ Successfully downloaded PDF: {output_path.name} ({file_size:,} bytes)")
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
    print(f"  ✓ Successfully downloaded HTML: {output_path.name} ({file_size:,} bytes)")
    return True

def get_paper_info_from_springer():
    """Try to get paper title/author info from Springer page."""
    try:
        # Get the abstract page to extract title/author info
        abstract_url = PAPER['springer_url'].replace('/content/pdf/', '/article/')
        response = requests.get(abstract_url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            # Try to extract title (basic extraction)
            content = response.text
            # Look for title in meta tags or h1
            import re
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if title_match:
                title = title_match.group(1).strip()
                # Clean up title
                title = re.sub(r'\s*-\s*.*$', '', title)  # Remove " - Springer" suffix
                return {'title': title}
    except Exception as e:
        print(f"  ⚠ Could not fetch Springer page: {e}")
    
    return None

def main():
    print("="*60)
    print("arXiv Paper Search and Download")
    print("="*60)
    print(f"DOI: {PAPER['doi']}")
    print(f"Springer URL: {PAPER['springer_url']}")
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    # Try to get paper info from Springer
    print("Step 1: Getting paper information from Springer...")
    paper_info = get_paper_info_from_springer()
    if paper_info:
        print(f"  Title: {paper_info.get('title', 'N/A')}")
    
    # Search arXiv by DOI first
    print("\nStep 2: Searching arXiv by DOI...")
    entries = search_arxiv_by_doi(PAPER['doi'])
    
    arxiv_id = None
    if entries:
        print(f"  Found {len(entries)} result(s)")
        for entry in entries:
            print(f"    - {entry.get('title', 'N/A')}")
            print(f"      Authors: {', '.join([a.get('name', '') for a in entry.get('authors', [])])}")
            arxiv_id = extract_arxiv_id(entry)
            if arxiv_id:
                print(f"      arXiv ID: {arxiv_id}")
                break
    
    # If not found, try searching by keywords if we have title
    if not arxiv_id and paper_info:
        print("\nStep 3: Searching arXiv by title keywords...")
        title = paper_info.get('title', '')
        if title:
            # Extract key words from title
            keywords = [w for w in title.split() if len(w) > 3][:5]  # Get first 5 meaningful words
            entries = search_arxiv_by_keywords(keywords)
            
            if entries:
                print(f"  Found {len(entries)} result(s)")
                # Look for best match
                for entry in entries:
                    entry_title = entry.get('title', '').lower()
                    if any(kw.lower() in entry_title for kw in keywords[:3]):
                        print(f"    Potential match: {entry.get('title', 'N/A')}")
                        arxiv_id = extract_arxiv_id(entry)
                        if arxiv_id:
                            print(f"      arXiv ID: {arxiv_id}")
                            break
    
    # Download if found
    if arxiv_id:
        print(f"\nStep 4: Downloading from arXiv (ID: {arxiv_id})...")
        
        pdf_path = OUTPUT_DIR / PAPER['pdf_filename']
        html_path = OUTPUT_DIR / PAPER['html_filename']
        
        try:
            download_arxiv_pdf(arxiv_id, pdf_path)
        except Exception as e:
            print(f"  ✗ Error downloading PDF: {e}")
        
        try:
            download_arxiv_html(arxiv_id, html_path)
        except Exception as e:
            print(f"  ✗ Error downloading HTML: {e}")
        
        print("\n✓ Successfully downloaded from arXiv!")
    else:
        print("\n✗ Paper not found on arXiv")
        print("  This paper may not have an arXiv preprint version")
        print("  The Springer PDF should still be available")

if __name__ == '__main__':
    main()
