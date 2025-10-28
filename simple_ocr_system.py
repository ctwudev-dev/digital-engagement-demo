import sys
from PIL import Image, ImageDraw
import pytesseract


def draw_boxes(image_path, output_path):
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    draw = ImageDraw.Draw(image)
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        text = data['text'][i]
        if text.strip():
            draw.rectangle([x, y, x + w, y + h], outline="red")
    image.save(output_path)


def main():
    if len(sys.argv) < 2:
        print("Usage: python simple_ocr_system.py <image_path> [output_image]")
        return
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output_with_boxes.png"
    # Extract and print text
    print("Extracted Text:")
    print(pytesseract.image_to_string(Image.open(image_path)))
    # Draw bounding boxes and save
    draw_boxes(image_path, output_path)
    print(f"Saved image with bounding boxes to {output_path}")


if __name__ == "__main__":
    main()
