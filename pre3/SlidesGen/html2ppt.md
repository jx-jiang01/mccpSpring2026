# HTML to PowerPoint (Editable Native Shapes)

Convert the UpANNS diagram (`poeOutput.html`) to a **fully editable** `poeOutput.pptx`.

All elements are native PowerPoint shapes — rectangles, text boxes, connectors,
freeform polygons, cylinder (CAN) shapes — individually selectable and editable.

## Setup

```bash
pip install -r requirements-html2ppt.txt
```

## Usage

```bash
python html2ppt.py
```

Outputs `poeOutput.pptx` in the same directory.

## How it works

1. Maps the SVG coordinate system (1300x560) to a widescreen slide (13.333" x 7.5").
2. Recreates every visual element as a native PowerPoint shape:
   - Rounded rectangles for section boxes
   - Small coloured squares for vector/grid cells
   - Cylinder (CAN) shapes for database icons
   - Freeform polygons for thick directional arrows
   - Connectors with arrowheads for flow lines
   - Text boxes for all labels
3. All shapes are individually editable — change colours, text, positions, etc.
