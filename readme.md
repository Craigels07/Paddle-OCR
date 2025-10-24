# PaddleOCR - Quick Start

- Install dependencies: `pip install -r requirements.txt`
- Put images in `input/` (png, jpg, jpeg, bmp, webp) one of the following:
- Run: `python paddle_ocr.py`
- Run: `python paddle_ocr_restructured.py`
- Run: `python paddle_pandasai.py`
- Outputs in `output/`: OCR JSON + annotated images; tables exported to `<image>_tables.xlsx`

Optional: For PDFs, convert pages to images or iterate pages via `PPStructure(..., img_idx=<page>)`.
