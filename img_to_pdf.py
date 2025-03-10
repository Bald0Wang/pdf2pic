import os
import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def img_to_pdf(input_path, output_pdf=None):
    # Generate default output PDF filename if not provided
    if output_pdf is None:
        if os.path.isfile(input_path):
            # If input is a file, use the filename without extension + .pdf
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_pdf = os.path.join(os.path.dirname(input_path), f"{base_name}.pdf")
        else:
            # If input is a directory, use the directory name + .pdf
            base_name = os.path.basename(input_path)
            output_pdf = os.path.join(input_path, f"{base_name}.pdf")
        print(f"No output filename specified. Using: {output_pdf}")

    if os.path.isfile(input_path):
        image_files = [input_path]
    elif os.path.isdir(input_path):
        image_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        image_files.sort()
    else:
        print("Invalid input path. Please provide a directory or an image file.")
        return

    if not image_files:
        print("No image files found in the input path.")
        return

    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        try:
            img = Image.open(image_file)
            img_width, img_height = img.size

            # Scale image to fit the page
            scale_x = letter[0] / float(img_width)
            scale_y = letter[1] / float(img_height)
            scale = min(scale_x, scale_y)

            img_width *= scale
            img_height *= scale

            x = (letter[0] - img_width) / 2
            y = (letter[1] - img_height) / 2

            c.drawImage(image_file, x, y, width=img_width, height=img_height)
            c.showPage()  # Start a new page for each image
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    c.save()
    print(f"Successfully created PDF: {output_pdf}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images in a directory to a PDF file.")
    parser.add_argument("input_path", help="Path to the input directory containing images or a single image file.")
    parser.add_argument("output_pdf", nargs='?', help="Path to the output PDF file. If not specified, the output will be saved in the same directory as the input.")
    args = parser.parse_args()

    img_to_pdf(args.input_path, args.output_pdf)
