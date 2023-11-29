import argparse
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, page_specifications):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_specification in page_specifications:
        if '-' in page_specification:
            start, end = map(int, page_specification.split('-'))
            for page_number in range(start, end + 1):
                writer.add_page(reader.pages[page_number - 1])
        else:
            page_number = int(page_specification)
            writer.add_page(reader.pages[page_number - 1])

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"Pages {', '.join(page_specifications)} extracted from {input_pdf} and saved to {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Create a new PDF file from specific pages of an existing PDF.")
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument("output_pdf", help="Output PDF file")
    parser.add_argument("page_specifications", nargs="+", help="Specify page numbers or ranges to extract (e.g., 1-3,18)")

    args = parser.parse_args()

    input_pdf = args.input_pdf
    output_pdf = args.output_pdf
    page_specifications = args.page_specifications

    extract_pages(input_pdf, output_pdf, page_specifications)

if __name__ == "__main__":
    main()