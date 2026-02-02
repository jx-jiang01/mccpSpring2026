#!/usr/bin/env python3
"""
MCP Server for Task 3.1: Paper Structure Visualization
OpenCode-Compatible Version - Can be called from GitHub without downloading
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Sequence

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    # Fallback for older MCP versions
    from mcp import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent

# Import our tool modules
from tools import file_tools, paper_tools, visualization_tools

# Initialize MCP server
app = Server("task3.1-visualizer")

# Get the base directory (works when called via OpenCode)
BASE_DIR = Path(__file__).parent


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools"""
    return [
        Tool(
            name="extract_archive",
            description="Extract a tar.gz or zip archive and return the structure and file paths",
            inputSchema={
                "type": "object",
                "properties": {
                    "archive_path": {
                        "type": "string",
                        "description": "Path to the archive file (tar.gz or zip)"
                    }
                },
                "required": ["archive_path"]
            }
        ),
        Tool(
            name="read_paper_file",
            description="Read and detect the format of a paper file (LaTeX .tex, HTML .html, or Markdown .md). PDF files are NOT supported.",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the paper file (must be .tex, .html, or .md format)"
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="fetch_arxiv_paper",
            description="Fetch a paper from arXiv by URL. Downloads LaTeX source (preferred) or HTML version. Returns path to local file.",
            inputSchema={
                "type": "object",
                "properties": {
                    "arxiv_url": {
                        "type": "string",
                        "description": "arXiv URL (e.g., https://arxiv.org/abs/1234.5678 or https://arxiv.org/pdf/1234.5678.pdf)"
                    },
                    "output_dir": {
                        "type": "string",
                        "description": "Optional: Directory to save the downloaded paper (default: ./arxiv_papers)"
                    }
                },
                "required": ["arxiv_url"]
            }
        ),
        Tool(
            name="parse_paper_structure",
            description="Parse a paper file and extract its hierarchical structure (sections, subsections, headings). Accepts LaTeX (.tex), HTML (.html), or Markdown (.md) files. PDF files are NOT supported.",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the paper file (.tex, .html, or .md format)"
                    },
                    "file_content": {
                        "type": "string",
                        "description": "Optional: Direct file content (if file_path not available)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="analyze_section_interconnections",
            description="Analyze relationships and interconnections between sections of a parsed paper",
            inputSchema={
                "type": "object",
                "properties": {
                    "structure_json": {
                        "type": "string",
                        "description": "JSON string of the parsed paper structure (from parse_paper_structure)"
                    },
                    "file_path": {
                        "type": "string",
                        "description": "Optional: Path to paper file for additional analysis"
                    }
                },
                "required": ["structure_json"]
            }
        ),
        Tool(
            name="generate_hierarchical_html",
            description="Generate a hierarchical HTML visualization of paper structure (Moodle-compatible)",
            inputSchema={
                "type": "object",
                "properties": {
                    "structure_json": {
                        "type": "string",
                        "description": "JSON string of the parsed paper structure"
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional: Output file path (default: visual.html in current directory)"
                    }
                },
                "required": ["structure_json"]
            }
        ),
        Tool(
            name="generate_interconnected_html",
            description="Generate an interactive network HTML visualization showing section interconnections with text excerpts",
            inputSchema={
                "type": "object",
                "properties": {
                    "structure_json": {
                        "type": "string",
                        "description": "JSON string of the parsed paper structure"
                    },
                    "connections_json": {
                        "type": "string",
                        "description": "JSON string of section interconnections (from analyze_section_interconnections)"
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional: Output file path (default: visual_interconnection_text.html)"
                    }
                },
                "required": ["structure_json", "connections_json"]
            }
        ),
        Tool(
            name="create_visualization_task",
            description="Complete workflow: extract archive, parse paper, and generate hierarchical visualization",
            inputSchema={
                "type": "object",
                "properties": {
                    "archive_path": {
                        "type": "string",
                        "description": "Path to the archive file"
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional: Output HTML file path"
                    }
                },
                "required": ["archive_path"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Handle tool calls"""
    
    try:
        if name == "extract_archive":
            result = await file_tools.extract_archive(arguments["archive_path"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "read_paper_file":
            result = await file_tools.read_paper_file(arguments["file_path"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "fetch_arxiv_paper":
            arxiv_url = arguments["arxiv_url"]
            output_dir = arguments.get("output_dir")
            result = await file_tools.fetch_arxiv_paper(arxiv_url, output_dir)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "parse_paper_structure":
            file_path = arguments.get("file_path")
            file_content = arguments.get("file_content")
            result = await paper_tools.parse_paper_structure(file_path, file_content)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "analyze_section_interconnections":
            structure_json = arguments["structure_json"]
            file_path = arguments.get("file_path")
            structure = json.loads(structure_json)
            result = await paper_tools.analyze_section_interconnections(structure, file_path)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "generate_hierarchical_html":
            structure_json = arguments["structure_json"]
            output_path = arguments.get("output_path")
            structure = json.loads(structure_json)
            result = await visualization_tools.generate_hierarchical_html(structure, output_path, BASE_DIR)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "generate_interconnected_html":
            structure_json = arguments["structure_json"]
            connections_json = arguments["connections_json"]
            output_path = arguments.get("output_path")
            structure = json.loads(structure_json)
            connections = json.loads(connections_json)
            result = await visualization_tools.generate_interconnected_html(
                structure, connections, output_path, BASE_DIR
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "create_visualization_task":
            archive_path = arguments["archive_path"]
            output_path = arguments.get("output_path")
            result = await workflow_complete_task(archive_path, output_path)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    except Exception as e:
        error_msg = {
            "error": str(e),
            "tool": name,
            "arguments": arguments
        }
        return [TextContent(type="text", text=json.dumps(error_msg, indent=2))]


async def workflow_complete_task(archive_path: str, output_path: str = None) -> dict:
    """Complete workflow: extract, parse, visualize"""
    # Extract archive
    extracted = await file_tools.extract_archive(archive_path)
    main_file = extracted.get("main_file")
    
    if not main_file:
        raise ValueError("Could not find main paper file in archive")
    
    # Parse structure
    structure = await paper_tools.parse_paper_structure(main_file)
    
    # Generate HTML
    if output_path is None:
        output_path = str(Path(main_file).parent / "visual.html")
    
    result = await visualization_tools.generate_hierarchical_html(structure, output_path, BASE_DIR)
    
    return {
        "status": "success",
        "extracted_files": extracted,
        "structure": structure,
        "output_file": result["output_path"]
    }


async def main():
    """Main entry point"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
