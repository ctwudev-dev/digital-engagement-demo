import pytesseract
from PIL import Image


def perform_ocr(image_path):
    """
    Simple OCR using pytesseract; returns extracted text from an image file.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print("Extracted text:")
    print(text)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OCR example using pytesseract.")
    parser.add_argument("image_path", help="Path to the image file to process")
    args = parser.parse_args()
    perform_ocr(args.image_path)
