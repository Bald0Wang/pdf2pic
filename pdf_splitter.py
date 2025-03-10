
import argparse
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_pdf, output_prefix="page", pages=None):
    reader = PdfReader(input_pdf)
    num_pages = len(reader.pages)

    if pages is None:
        pages = range(num_pages)
    else:
        pages = [int(p) - 1 for p in pages.split(",")]  # Convert to 0-based indexing

    for i in pages:
        if 0 <= i < num_pages:
            writer = PdfWriter()
            writer.add_page(reader.pages[i])
            output_filename = f"{output_prefix}_{i + 1}.pdf"
            with open(output_filename, "wb") as output_file:
                writer.write(output_file)
            print(f"Page {i + 1} saved to {output_filename}")
        else:
            print(f"Invalid page number: {i + 1}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a PDF file into individual pages.")
    parser.add_argument("input_pdf", help="Path to the input PDF file.")
    parser.add_argument("-o", "--output_prefix", default="page", help="Prefix for the output PDF files (default: page).")
    parser.add_argument("-p", "--pages", help="Comma-separated list of page numbers to extract (e.g., 1,3,5). If not specified, all pages will be extracted.")

    args = parser.parse_args()

    split_pdf(args.input_pdf, args.output_prefix, args.pages)
