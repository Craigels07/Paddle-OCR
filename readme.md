# PaddleOCR Test Repository

This repository provides **two options** for running OCR locally on your machine:

1. **Basic PaddleOCR** (`paddle_ocr_basic.py`) - Lightweight, fast, simple text extraction
2. **PaddleOCR-VL** (`paddle_ocr_test_script.py`) - Advanced document understanding with 0.9B Vision-Language model

Both run **100% locally** - no API calls, no internet required after initial model download.

## Features

### Basic PaddleOCR (Recommended for most users)
- ⚡ **Lightweight**: ~150MB models, fast inference
- 🖼️ **Image Support**: Process PNG, JPG, and other image formats
- 💾 **Runs Offline**: 100% local processing after initial setup
- 🎯 **Multilingual**: Supports 80+ languages
- 📝 **Simple Output**: Plain text extraction with confidence scores

### PaddleOCR-VL (Advanced users)
- 🤖 **Vision-Language Model**: 0.9B parameters for intelligent document parsing
- 📄 **PDF Support**: Process multi-page documents
- 🌐 **URL Support**: Can process images directly from URLs
- 📊 **Structured Output**: JSON and Markdown formats
- 📝 **Document Understanding**: Advanced layout analysis

## Quick Start

### Option 1: Basic PaddleOCR (Recommended)

**Prerequisites**: Python 3.7+

```bash
# Install dependencies
pip install -r requirements_basic.txt

# Run the script
python paddle_ocr_basic.py
```

This will:
- Download models (~150MB) on first run
- Create a test image
- Extract text and save to `ocr_results_basic.txt`
- **Everything runs locally on your machine**

### Option 2: PaddleOCR-VL (Advanced)

**Prerequisites**: Python 3.8+, PaddlePaddle 3.0+

```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python paddle_ocr_test_script.py
```

This will:
- Download models (~1GB) on first run
- Create a test image
- Extract text with document structure
- Save results to `output/` directory in JSON and Markdown formats
- **Everything runs locally on your machine**

## Usage

### Quick Start

Run the test script to verify installation:

```bash
python paddle_ocr_test_script.py
```

This will automatically create a test image and perform OCR on it.

### Using Your Own Files

Edit `paddle_ocr_test_script.py` and add your file paths:

```python
if __name__ == "__main__":
    # Test with local files
    run_ocr('path/to/your/image.jpg')
    run_ocr('path/to/your/document.pdf')
    
    # Test with URLs
    run_ocr('https://example.com/document.png')
    
    # Specify custom output directory
    run_ocr('receipt.jpg', output_dir='my_results')
```

Or use the function directly in your code:

```python
from paddle_ocr_test_script import run_ocr

# Process local file (saves to 'output/' directory by default)
run_ocr('receipt.jpg')

# Process URL with custom output directory
run_ocr('https://example.com/invoice.pdf', output_dir='invoices')
```

**Output**: Results are automatically saved in both JSON and Markdown formats in the specified output directory.

## Configuration

### GPU Acceleration

For better performance, install the GPU version of PaddlePaddle:

```bash
# For CUDA 11.6
pip install paddlepaddle-gpu==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu116/

# For CUDA 12.6
pip install paddlepaddle-gpu==3.2.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
```

PaddleOCR-VL will automatically detect and use GPU if available.

### Advanced Options

You can customize the pipeline initialization:

```python
from paddleocr import PaddleOCRVL

# Use optimized inference server (requires Docker)
pipeline = PaddleOCRVL(
    vl_rec_backend="vllm-server",
    vl_rec_server_url="http://127.0.0.1:8080/v1"
)
```

See the [official documentation](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html) for more configuration options.

## Output Format

PaddleOCR-VL automatically saves results in two formats:

### JSON Format (`output/page_1.json`)
Contains structured data with:
- Detected text content
- Bounding boxes and coordinates
- Confidence scores
- Layout information
- Document structure

### Markdown Format (`output/page_1.md`)
Human-readable format with:
- Extracted text in reading order
- Preserved document structure
- Easy to review and edit

## Project Structure

```text
Paddle-OCR/
├── paddle_ocr_test_script.py  # Main OCR script
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Dependencies

- `paddlepaddle>=3.0.0` - Deep learning framework
- `paddleocr[doc-parser]>=2.9.0` - OCR toolkit with document parser
- `Pillow>=10.0.0` - Image processing

The `[doc-parser]` extra includes all dependencies needed for PDF processing and document understanding.

## Troubleshooting

### "No module named 'paddleocr'"

```bash
pip install -U "paddleocr[doc-parser]"
```

### Model download is slow

Models are downloaded automatically on first run (~1GB). Be patient or use a mirror:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

### Out of memory errors

PaddleOCR-VL requires ~2GB GPU memory. If you encounter OOM errors:
- Use CPU mode (slower but works)
- Process smaller images
- Use the optimized inference server (Docker)

## References

- [PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR)
- [PaddleOCR Documentation](https://paddlepaddle.github.io/PaddleOCR/)
- [PaddleOCR-VL on HuggingFace](https://huggingface.co/PaddlePaddle/PaddleOCR-VL)

## License

This project is for testing and educational purposes. PaddleOCR is licensed under Apache 2.0.
