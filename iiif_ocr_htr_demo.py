"""
IIIF and OCR/HTR Demo

This script demonstrates how to retrieve images from an IIIF manifest, perform OCR/HTR processing, and output the recognized text.

Requirements:
- requests
- pillow
- pytesseract

Note: This script assumes network access to the IIIF server.
"""

import json
import requests
from PIL import Image
import pytesseract
from io import BytesIO


def download_image_from_iiif(image_url):
    """Download an image from a IIIF image API URL and return a PIL Image."""
    response = requests.get(image_url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))


def preprocess_image_for_ocr(image):
    """Convert image to grayscale and apply binary threshold to improve OCR/HTR results."""
    gray = image.convert("L")
    bw = gray.point(lambda x: 0 if x < 128 else 255, "1")
    return bw


def run_ocr(image, lang="eng"):
    """Run OCR/HTR on a PIL Image using Tesseract. For handwriting, ensure the appropriate language model is installed."""
    processed = preprocess_image_for_ocr(image)
    return pytesseract.image_to_string(processed, lang=lang, config="--oem 1 --psm 6")


def process_manifest(manifest_url, lang="eng"):
    """Load a IIIF manifest, iterate through its canvases, download each image, perform OCR/HTR, and return results."""
    manifest_data = requests.get(manifest_url).json()
    sequences = manifest_data.get("sequences", [])
    results = []
    if not sequences:
        return results
    canvases = sequences[0].get("canvases", [])
    for canvas in canvases:
        canvas_id = canvas.get("@id")
        image_service = canvas["images"][0]["resource"]["service"]["@id"]
        image_url = f"{image_service}/full/full/0/default.jpg"
        img = download_image_from_iiif(image_url)
        extracted_text = run_ocr(img, lang=lang)
        results.append({"canvas_id": canvas_id, "text": extracted_text})
    return results


if __name__ == "__main__":
    manifest_url = input("Enter IIIF manifest URL: ").strip()
    language = input("Enter Tesseract language code (default 'eng'): ").strip() or "eng"
    output = process_manifest(manifest_url, lang=language)
    for item in output:
        print(f"Canvas: {item['canvas_id']}")
        print("Extracted Text:")
        print(item['text'])
        print("-" * 40)
