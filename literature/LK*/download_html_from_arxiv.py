#!/usr/bin/env python3
"""
Download HTML versions of papers from arXiv.
arXiv provides HTML versions which are machine-readable and easier to process.
"""

import requests
from pathlib import Path
import time

# Papers with their arXiv IDs (already found)
PAPERS = [
    {
        'doi': '10.1145/3705328.3748167',
        'arxiv_id': '2507.17290v1',
        'title': 'Exploring the Potential of LLMs for Serendipity Evaluation in Recommender Systems',
        'html_filename': 'paper1_3705328_3748167.html'
    },
    {
        'doi': '10.1145/3726302.3729893',
        'arxiv_id': '2410.20027v2',
        'title': 'Agentic Feedback Loop Modeling Improves Recommendation and User Simulation',
        'html_filename': 'paper2_3726302_3729893.html'
    }
]

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

def download_arxiv_html(arxiv_id, output_path):
    """Download HTML version from arXiv."""
    # Try different HTML URLs that arXiv might use
    html_urls = [
        f"https://arxiv.org/html/{arxiv_id}",  # HTML version
        f"https://arxiv.org/abs/{arxiv_id}",    # Abstract page (contains HTML content)
    ]
    
    print(f"  arXiv ID: {arxiv_id}")
    
    for url in html_urls:
        try:
            print(f"  Trying: {url}")
            response = requests.get(url, timeout=60, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            })
            response.raise_for_status()
            
            content_type = response.headers.get('Content-Type', '').lower()
            
            if 'text/html' in content_type:
                # Save the HTML
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                
                file_size = output_path.stat().st_size
                print(f"  ✓ Successfully downloaded HTML: {output_path.name} ({file_size:,} bytes)")
                return True
            else:
                print(f"  ⚠ URL returned {content_type}, not HTML")
                
        except Exception as e:
            print(f"  ⚠ Error with {url}: {e}")
            continue
    
    return False

def get_source_tex_or_html(arxiv_id):
    """Try to get the source HTML/TeX from arXiv."""
    # Sometimes arXiv has the source available
    source_urls = [
        f"https://arxiv.org/e-print/{arxiv_id}",  # Source (usually tar.gz or PDF)
        f"https://arxiv.org/src/{arxiv_id}",      # Alternative source URL
    ]
    
    for url in source_urls:
        try:
            response = requests.head(url, timeout=30, allow_redirects=True)
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '')
                print(f"  Found source at: {url} ({content_type})")
                return url
        except:
            continue
    
    return None

def main():
    print("="*60)
    print("arXiv HTML Paper Downloader")
    print("="*60)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    results = []
    for i, paper in enumerate(PAPERS, 1):
        print(f"\n[{i}/{len(PAPERS)}] Processing: {paper['doi']}")
        print(f"  Title: {paper['title']}")
        print(f"  arXiv ID: {paper['arxiv_id']}")
        
        output_path = OUTPUT_DIR / paper['html_filename']
        
        try:
            success = download_arxiv_html(paper['arxiv_id'], output_path)
            
            if success:
                results.append((paper['doi'], True))
                print(f"  ✓ Success!")
            else:
                # Try getting source information
                print(f"  Trying alternative methods...")
                source_url = get_source_tex_or_html(paper['arxiv_id'])
                if source_url:
                    print(f"  Note: Source available at {source_url}")
                
                results.append((paper['doi'], False))
                print(f"  ✗ Could not download HTML version")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
            results.append((paper['doi'], False))
        
        if i < len(PAPERS):
            print("\n  Waiting 2 seconds before next download...")
            time.sleep(2)
    
    print("\n" + "="*60)
    print("Summary:")
    print("="*60)
    for doi, success in results:
        status = "✓ Downloaded" if success else "✗ Failed"
        print(f"  {doi}: {status}")
    
    print("\nNote: If HTML download failed, the papers may:")
    print("  - Only be available in PDF format on arXiv")
    print("  - Require manual extraction from the abstract page")
    print("  - Be available in the abstract page HTML (which was downloaded)")

if __name__ == '__main__':
    main()
