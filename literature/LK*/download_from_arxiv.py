#!/usr/bin/env python3
"""
Search arXiv for papers and download PDFs if available.
arXiv PDFs are open access and much easier to download than ACM.
"""

import requests
import feedparser
from pathlib import Path
import time
import re

# Papers to search for
PAPERS = [
    {
        'doi': '10.1145/3705328.3748167',
        'title_keywords': ['serendipity', 'LLM', 'recommender'],
        'author_keywords': ['Li Kang', 'Kang'],
        'filename': 'paper1_3705328_3748167.pdf'
    },
    {
        'doi': '10.1145/3726302.3729893',
        'title_keywords': ['Agentic', 'Feedback Loop', 'Recommendation'],
        'author_keywords': ['Cai', 'Zhang'],
        'filename': 'paper2_3726302_3729893.pdf'
    }
]

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

def search_arxiv(query, max_results=20):
    """Search arXiv using the API."""
    url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results,
        'sortBy': 'relevance',
        'sortOrder': 'descending'
    }
    
    print(f"  Searching arXiv for: {query}")
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    
    feed = feedparser.parse(response.content)
    return feed.entries

def extract_arxiv_id(entry):
    """Extract arXiv ID from entry."""
    # arXiv ID is usually in the link or id field
    link = entry.get('id', '')
    # Format: http://arxiv.org/abs/1234.5678v1
    match = re.search(r'arxiv\.org/abs/([\d.]+v?\d*)', link)
    if match:
        return match.group(1)
    return None

def download_arxiv_pdf(arxiv_id, output_path):
    """Download PDF from arXiv."""
    # arXiv PDF URL format: https://arxiv.org/pdf/{arxiv_id}.pdf
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    
    print(f"  Downloading PDF from: {pdf_url}")
    response = requests.get(pdf_url, timeout=60, stream=True)
    response.raise_for_status()
    
    # Check if it's actually a PDF
    content_type = response.headers.get('Content-Type', '')
    if 'application/pdf' not in content_type:
        # Sometimes arXiv redirects, check the actual content
        first_bytes = response.content[:4]
        if first_bytes != b'%PDF':
            raise ValueError(f"Expected PDF but got {content_type}")
    
    # Save the PDF
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    
    file_size = output_path.stat().st_size
    print(f"  ✓ Successfully downloaded: {output_path.name} ({file_size:,} bytes)")
    return True

def find_and_download_paper(paper_info):
    """Search for a paper on arXiv and download if found."""
    print(f"\n{'='*60}")
    print(f"Processing: {paper_info['doi']}")
    print(f"{'='*60}")
    
    # Try multiple search queries
    search_queries = [
        ' '.join(paper_info['title_keywords']),
        ' '.join(paper_info['author_keywords'] + paper_info['title_keywords'][:2]),
        paper_info['doi'].replace('10.1145/', ''),
    ]
    
    for query in search_queries:
        try:
            entries = search_arxiv(query, max_results=10)
            
            if not entries:
                print(f"  No results found for query: {query}")
                continue
            
            print(f"  Found {len(entries)} results")
            
            # Look for matching paper
            for entry in entries:
                title = entry.get('title', '').lower()
                authors = ' '.join([a.get('name', '') for a in entry.get('authors', [])]).lower()
                
                # Check if this might be our paper
                title_match = any(kw.lower() in title for kw in paper_info['title_keywords'])
                author_match = any(kw.lower() in authors for kw in paper_info['author_keywords'])
                
                if title_match or author_match:
                    print(f"\n  Potential match found:")
                    print(f"    Title: {entry.get('title', 'N/A')}")
                    print(f"    Authors: {', '.join([a.get('name', '') for a in entry.get('authors', [])])}")
                    print(f"    Published: {entry.get('published', 'N/A')}")
                    
                    arxiv_id = extract_arxiv_id(entry)
                    if arxiv_id:
                        print(f"    arXiv ID: {arxiv_id}")
                        
                        # Download the PDF
                        output_path = OUTPUT_DIR / paper_info['filename']
                        try:
                            download_arxiv_pdf(arxiv_id, output_path)
                            return True
                        except Exception as e:
                            print(f"  ✗ Error downloading PDF: {e}")
                            continue
                    else:
                        print(f"  ⚠ Could not extract arXiv ID from: {entry.get('id', 'N/A')}")
            
            print(f"  No matching paper found in results for query: {query}")
            
        except Exception as e:
            print(f"  ✗ Error searching arXiv: {e}")
            continue
    
    print(f"\n  ✗ Could not find or download paper from arXiv")
    print(f"  Note: This paper may not have an arXiv preprint")
    return False

def main():
    print("="*60)
    print("arXiv Paper Downloader")
    print("="*60)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    results = []
    for i, paper in enumerate(PAPERS, 1):
        print(f"\n[{i}/{len(PAPERS)}] Searching for paper...")
        success = find_and_download_paper(paper)
        results.append((paper['doi'], success))
        
        if i < len(PAPERS):
            print("\n  Waiting 2 seconds before next search...")
            time.sleep(2)
    
    print("\n" + "="*60)
    print("Summary:")
    print("="*60)
    for doi, success in results:
        status = "✓ Downloaded" if success else "✗ Not found on arXiv"
        print(f"  {doi}: {status}")
    
    print("\nNote: If papers were not found on arXiv, they may:")
    print("  - Not have arXiv preprints (some ACM papers don't)")
    print("  - Be published only in ACM (no preprint version)")
    print("  - Need manual download from ACM website")

if __name__ == '__main__':
    main()
