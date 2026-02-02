"""File operation tools for extracting and reading paper files"""

import tarfile
import zipfile
import os
import re
import urllib.request
import urllib.parse
from pathlib import Path
from typing import Dict, List, Optional


async def extract_archive(archive_path: str) -> Dict:
    """Extract a tar.gz or zip archive"""
    archive_path = Path(archive_path).expanduser().resolve()
    
    if not archive_path.exists():
        raise FileNotFoundError(f"Archive not found: {archive_path}")
    
    # Determine extraction directory
    extract_dir = archive_path.parent / f"{archive_path.stem}_extracted"
    extract_dir.mkdir(exist_ok=True)
    
    files = []
    main_file = None
    
    try:
        if archive_path.suffix == '.gz' or '.tar' in archive_path.suffixes:
            # Handle tar.gz
            with tarfile.open(archive_path, 'r:gz') as tar:
                tar.extractall(extract_dir)
                files = [str(extract_dir / member.name) for member in tar.getmembers() if member.isfile()]
        
        elif archive_path.suffix == '.zip':
            # Handle zip
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
                files = [str(extract_dir / name) for name in zip_ref.namelist() if not name.endswith('/')]
        
        # Find main paper file (LaTeX .tex, HTML, or Markdown - PDF not supported)
        for file_path in files:
            file_path_obj = Path(file_path)
            if file_path_obj.suffix in ['.tex', '.html', '.htm', '.md']:
                # Prefer .tex files, then HTML, then markdown
                if main_file is None or file_path_obj.suffix == '.tex':
                    main_file = str(file_path_obj)
                elif main_file and Path(main_file).suffix != '.tex' and file_path_obj.suffix in ['.html', '.htm']:
                    main_file = str(file_path_obj)
        
        return {
            "status": "success",
            "extract_dir": str(extract_dir),
            "files": files,
            "main_file": main_file,
            "file_count": len(files)
        }
    
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "extract_dir": str(extract_dir)
        }


async def read_paper_file(file_path: str) -> Dict:
    """Read and detect format of a paper file"""
    file_path = Path(file_path).expanduser().resolve()
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_format = file_path.suffix.lower()
    
    try:
        if file_format == '.tex':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            return {
                "status": "success",
                "file_path": str(file_path),
                "format": "latex",
                "content": content[:10000],  # First 10k chars for preview
                "full_content_available": True
            }
        
        elif file_format in ['.html', '.htm']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            return {
                "status": "success",
                "file_path": str(file_path),
                "format": "html",
                "content": content[:10000],  # First 10k chars for preview
                "full_content_available": True
            }
        
        elif file_format in ['.md', '.markdown']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            return {
                "status": "success",
                "file_path": str(file_path),
                "format": "markdown",
                "content": content,
                "full_content_available": True
            }
        
        else:
            return {
                "status": "unknown_format",
                "file_path": str(file_path),
                "format": file_format,
                "note": "Format not directly supported, attempting text read"
            }
    
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "file_path": str(file_path)
        }


async def fetch_arxiv_paper(arxiv_url: str, output_dir: Optional[str] = None) -> Dict:
    """Fetch LaTeX source from arXiv and save to local file"""
    
    # Extract arXiv ID from URL
    # Supports formats: https://arxiv.org/abs/1234.5678, https://arxiv.org/pdf/1234.5678.pdf, arxiv.org/abs/1234.5678v2
    arxiv_id_match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?', arxiv_url)
    
    if not arxiv_id_match:
        raise ValueError(f"Invalid arXiv URL format: {arxiv_url}. Expected format: https://arxiv.org/abs/1234.5678")
    
    arxiv_id = arxiv_id_match.group(1)
    
    # Try to get LaTeX source (tar.gz)
    latex_source_url = f"https://arxiv.org/src/{arxiv_id}"
    
    if output_dir is None:
        output_dir = Path.cwd() / "arxiv_papers"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Try to download source
    tar_path = output_dir / f"{arxiv_id}.tar.gz"
    
    try:
        # Try downloading source tar.gz
        urllib.request.urlretrieve(latex_source_url, tar_path)
        
        # Extract and find main .tex file
        extracted = await extract_archive(str(tar_path))
        
        if extracted.get("main_file"):
            return {
                "status": "success",
                "arxiv_id": arxiv_id,
                "source_url": latex_source_url,
                "tar_file": str(tar_path),
                "extracted_dir": extracted.get("extract_dir"),
                "main_file": extracted.get("main_file"),
                "format": "latex"
            }
        else:
            raise ValueError("Could not find LaTeX source file in arXiv archive")
    
    except Exception as e:
        # If source download fails, try HTML version
        html_url = f"https://arxiv.org/html/{arxiv_id}"
        html_path = output_dir / f"{arxiv_id}.html"
        
        try:
            urllib.request.urlretrieve(html_url, html_path)
            return {
                "status": "success",
                "arxiv_id": arxiv_id,
                "source_url": html_url,
                "html_file": str(html_path),
                "format": "html",
                "note": "LaTeX source not available, using HTML version"
            }
        except Exception as html_error:
            return {
                "status": "error",
                "error": f"Failed to fetch both LaTeX source and HTML: {str(e)}, HTML: {str(html_error)}",
                "arxiv_id": arxiv_id
            }
