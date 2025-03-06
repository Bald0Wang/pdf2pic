import argparse
import os
import fitz  # PyMuPDF

def convert_pdf_to_images(pdf_path, output_dir, dpi=200, fmt='png', split_height=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        if split_height and split_height > 0:
            total_height = int(page.rect.height)
            split_height = int(split_height)
            for part, y in enumerate(range(0, total_height, split_height)):
                clip = fitz.Rect(0, y, page.rect.width, min(y+split_height, total_height))
                pix = page.get_pixmap(dpi=dpi, clip=clip)
                output_path = os.path.join(output_dir, f'page_{i+1:03d}_part{part+1}.{fmt}')
                pix.save(output_path)
                print(f'Saved: {output_path}')
        else:
            pix = page.get_pixmap(dpi=dpi)
            output_path = os.path.join(output_dir, f'page_{i+1:03d}.{fmt}')
            pix.save(output_path)
            print(f'Saved: {output_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert PDF pages to images')
    parser.add_argument('input_pdf', help='Input PDF file path')
    parser.add_argument('-o', '--output', default='output', help='Output directory')
    parser.add_argument('--dpi', type=int, default=200, help='Image resolution (default: 200)')
    parser.add_argument('--format', choices=['png', 'jpg'], default='png', help='Output format (default: png)')
    parser.add_argument('--split-height', type=int, help='垂直切割高度（像素）')
    
    args = parser.parse_args()
    
    try:
        convert_pdf_to_images(args.input_pdf, args.output, args.dpi, args.format, args.split_height)
        print(f'Successfully converted {os.path.basename(args.input_pdf)}')
    except Exception as e:
        print(f'Error: {str(e)}')
