from paddleocr import PaddleOCR
import os
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, 'input')
OUTPUT_PATH = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_PATH, exist_ok=True)

print("Initializing PaddleOCR (basic mode)... (This may take a moment)")
ocr = PaddleOCR(
    use_doc_orientation_classify=False, # Disables document orientation classification model via this parameter
    use_doc_unwarping=False, # Disables text image rectification model via this parameter
    use_textline_orientation=False, # Disables text line orientation classification model via this parameter
)
# ocr = PaddleOCR(lang="en") # Uses English model by specifying language parameter
# ocr = PaddleOCR(ocr_version="PP-OCRv4") # Uses other PP-OCR versions via version parameter
# ocr = PaddleOCR(device="gpu") # Enables GPU acceleration for model inference via device parameter
# ocr = PaddleOCR(
#     text_detection_model_name="PP-OCRv5_mobile_det",
#     text_recognition_model_name="PP-OCRv5_mobile_rec",
#     use_doc_orientation_classify=False,
#     use_doc_unwarping=False,
#     use_textline_orientation=False,
# ) # Switch to PP-OCRv5_mobile models


image_files = []
for ext in ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.webp'):
    image_files.extend(glob.glob(os.path.join(INPUT_PATH, ext)))

if not image_files:
    print(f"Error: No images found in {INPUT_PATH}")
    print("Please add some images (.png, .jpg, etc.) to your input folder.")
    exit()

print(f"Found {len(image_files)} images to process...")

for image_path in image_files:
    filename = os.path.basename(image_path)
    base_filename = os.path.splitext(filename)[0]
    print(f"\n--- Processing: {filename} ---")
    print("Running OCR on:  " + image_path)
    result = ocr.predict(image_path)
    for res in result:
        res.print()
        res.save_to_img(OUTPUT_PATH)
        res.save_to_json(OUTPUT_PATH)