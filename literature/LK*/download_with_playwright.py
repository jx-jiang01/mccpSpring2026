#!/usr/bin/env python3
"""
Download ACM papers using Playwright (handles Cloudflare protection properly).

Installation:
    pip install playwright
    playwright install chromium

Usage:
    python3 download_with_playwright.py
"""

from playwright.sync_api import sync_playwright
import time
from pathlib import Path

# Papers to download
PAPERS = [
    {
        'doi': '10.1145/3705328.3748167',
        'url': 'https://dl.acm.org/doi/pdf/10.1145/3705328.3748167',
        'filename': 'paper1_3705328_3748167.pdf'
    },
    {
        'doi': '10.1145/3726302.3729893',
        'url': 'https://dl.acm.org/doi/pdf/10.1145/3726302.3729893',
        'filename': 'paper2_3726302_3729893.pdf'
    }
]

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

def download_paper(playwright, paper):
    """Download a paper using Playwright browser automation."""
    browser = playwright.chromium.launch(headless=False)  # headless=False to see what's happening
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    page = context.new_page()
    
    try:
        print(f"  Navigating to PDF URL: {paper['url']}")
        page.goto(paper['url'], wait_until='networkidle', timeout=60000)
        
        # Wait for Cloudflare challenge if present
        print("  Waiting for page to load (including Cloudflare verification if needed)...")
        time.sleep(5)
        
        # Check if we got a PDF or an HTML page
        content_type = page.evaluate('''() => {
            return document.contentType || 'unknown';
        }''')
        
        print(f"  Content type detected: {content_type}")
        
        # Try to find and click cookie consent if present
        try:
            # Look for common cookie consent buttons
            cookie_selectors = [
                'button:has-text("Allow all cookies")',
                'button:has-text("Accept all")',
                'button:has-text("Accept")',
                '[id*="cookie"] button',
                '[class*="cookie"] button'
            ]
            
            for selector in cookie_selectors:
                if page.query_selector(selector):
                    print(f"  Clicking cookie consent: {selector}")
                    page.click(selector, timeout=3000)
                    time.sleep(2)
                    break
        except:
            pass  # No cookie consent found, continue
        
        # Wait a bit more for any dynamic content
        time.sleep(3)
        
        # Check if we have a PDF embedded or if we need to follow a link
        # If the page contains a PDF embed, we might need to get the actual PDF URL
        page_content = page.content()
        
        # Check if it's actually a PDF page
        if 'application/pdf' in content_type or page.url.endswith('.pdf'):
            print(f"  PDF detected, downloading...")
            
            # Wait for PDF to load
            time.sleep(3)
            
            # Use Playwright's download functionality
            with page.expect_download() as download_info:
                # Try to trigger download (right-click save or direct link)
                page.evaluate('''() => {
                    // Try to find PDF download link
                    const links = document.querySelectorAll('a[href*="pdf"], a[href*="PDF"]');
                    if (links.length > 0) {
                        links[0].click();
                        return true;
                    }
                    // Otherwise, try to save the current page if it's a PDF
                    return false;
                }''')
                time.sleep(2)
            
            # Alternative: Direct download via request
            try:
                response = page.request.get(paper['url'])
                if response.ok and 'application/pdf' in response.headers.get('content-type', ''):
                    filepath = OUTPUT_DIR / paper['filename']
                    filepath.write_bytes(response.body())
                    print(f"  ✓ Successfully downloaded: {paper['filename']}")
                    print(f"  File size: {filepath.stat().st_size:,} bytes")
                    return True
            except Exception as e:
                print(f"  ⚠ Direct download attempt failed: {e}")
            
            # If we got here, try to save via browser download
            try:
                download = download_info.value
                filepath = OUTPUT_DIR / paper['filename']
                download.save_as(filepath)
                print(f"  ✓ Successfully downloaded via browser: {paper['filename']}")
                return True
            except:
                pass
        
        # If we still don't have the PDF, try accessing the abstract page first
        print("  PDF not directly accessible, trying via abstract page...")
        abstract_url = paper['url'].replace('/pdf/', '/')
        page.goto(abstract_url, wait_until='networkidle', timeout=60000)
        time.sleep(5)
        
        # Look for PDF download link
        pdf_link = page.query_selector('a[href*="/pdf/"], a[href*="PDF"], a:has-text("PDF"), a:has-text("Download PDF")')
        if pdf_link:
            print("  Found PDF link on abstract page, clicking...")
            pdf_link.click()
            time.sleep(5)
            
            # Try download again
            response = page.request.get(paper['url'])
            if response.ok:
                filepath = OUTPUT_DIR / paper['filename']
                filepath.write_bytes(response.body())
                print(f"  ✓ Successfully downloaded: {paper['filename']}")
                return True
        
        print(f"  ✗ Could not download {paper['filename']} automatically")
        print(f"  Please try manual download from: {paper['url']}")
        return False
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False
    finally:
        browser.close()

def main():
    print("="*60)
    print("ACM Paper Downloader using Playwright")
    print("="*60)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    with sync_playwright() as playwright:
        for i, paper in enumerate(PAPERS, 1):
            print(f"\n[{i}/{len(PAPERS)}] Processing: {paper['doi']}")
            print(f"  Title: {paper.get('title', 'N/A')}")
            success = download_paper(playwright, paper)
            if i < len(PAPERS):
                print("\n  Waiting 3 seconds before next download...")
                time.sleep(3)
    
    print("\n" + "="*60)
    print("Download process completed!")
    print("="*60)

if __name__ == '__main__':
    main()
