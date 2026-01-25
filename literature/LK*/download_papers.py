#!/usr/bin/env python3
"""
Script to download ACM papers in machine-readable format (PDF).
ACM is now fully open access as of January 2026, so papers should be freely accessible.
"""

import requests
from pathlib import Path
import time

# Set up session to maintain cookies
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})

# URLs to download
papers = [
    {
        'url': 'https://dl.acm.org/doi/pdf/10.1145/3705328.3748167',
        'filename': 'paper1_3705328_3748167.pdf'
    },
    {
        'url': 'https://dl.acm.org/doi/pdf/10.1145/3726302.3729893',
        'filename': 'paper2_3726302_3729893.pdf'
    }
]

# Output directory
output_dir = Path(__file__).parent
output_dir.mkdir(exist_ok=True)

print("Status: Starting paper downloads...")
print(f"Output directory: {output_dir}")

for i, paper in enumerate(papers, 1):
    print(f"\n[{i}/{len(papers)}] Processing: {paper['url']}")
    
    # First, visit the abstract page to get cookies
    abstract_url = paper['url'].replace('/pdf/', '/')
    print(f"  Step 1: Accessing abstract page for cookies...")
    try:
        response = session.get(abstract_url, timeout=30, allow_redirects=True)
        print(f"  Status: Abstract page accessed (Status: {response.status_code})")
        time.sleep(2)  # Wait a bit for Cloudflare if needed
    except Exception as e:
        print(f"  Warning: Could not access abstract page: {e}")
    
    # Now try to download the PDF
    print(f"  Step 2: Downloading PDF...")
    try:
        response = session.get(paper['url'], timeout=60, allow_redirects=True, stream=True)
        print(f"  Status: PDF request response (Status: {response.status_code})")
        print(f"  Headers: Content-Type: {response.headers.get('Content-Type', 'N/A')}")
        
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            
            if 'application/pdf' in content_type:
                # It's a PDF, save it
                filepath = output_dir / paper['filename']
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                file_size = filepath.stat().st_size
                print(f"  ✓ Success: Downloaded {paper['filename']} ({file_size:,} bytes)")
                
                # Verify it's actually a PDF
                with open(filepath, 'rb') as f:
                    header = f.read(4)
                    if header == b'%PDF':
                        print(f"  ✓ Verified: File is a valid PDF")
                    else:
                        print(f"  ⚠ Warning: File might not be a valid PDF (header: {header})")
            else:
                # Check if it's an HTML redirect/challenge page
                content = response.text[:500]
                if 'Cloudflare' in content or 'challenge' in content.lower():
                    print(f"  ⚠ Warning: Received Cloudflare challenge page instead of PDF")
                    print(f"  Status: Manual browser access may be required")
                else:
                    print(f"  ⚠ Warning: Unexpected content type: {content_type}")
                    print(f"  Content preview: {content[:200]}")
        else:
            print(f"  ✗ Error: HTTP {response.status_code}")
            print(f"  Response preview: {response.text[:200]}")
            
    except Exception as e:
        print(f"  ✗ Error downloading PDF: {e}")

print("\n" + "="*60)
print("Status: Download process completed")
print("="*60)
