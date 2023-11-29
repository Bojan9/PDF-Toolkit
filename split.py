import argparse
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_folder):
    reader = PdfReader(input_pdf)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for page_number, page in enumerate(reader.pages, 1):
        output_filename = os.path.join(output_folder, f"page_{page_number}.pdf")

        # Write each page to a separate PDF file
        with open(output_filename, "wb") as output_file:
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(output_file)

        print(f"Page {page_number} saved to {output_filename}")

def main():
    parser = argparse.ArgumentParser(description="Split a PDF file into individual pages.")
    parser.add_argument("input_pdf", help="Input PDF file to split")
    parser.add_argument("--output", default="split_pages", help="Output folder for individual pages (default: split_pages)")

    args = parser.parse_args()

    input_pdf = args.input_pdf
    output_folder = args.output

    split_pdf(input_pdf, output_folder)

if __name__ == "__main__":
    main()