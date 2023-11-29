import argparse
from PyPDF2 import PdfReader

def extract_text(pdf_file, output_text_file, page_number=None):
    reader = PdfReader(pdf_file)

    extracted_text = ""
    
    if page_number is None:
        for page in reader.pages:
            extracted_text += page.extract_text()
    else:
        page = reader.pages[page_number - 1]
        extracted_text = page.extract_text()

    with open(output_text_file, "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)

    print(f"Text extracted from {pdf_file} (Page {page_number if page_number else 'All'}) and saved to {output_text_file}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file and save it to a text document.")
    parser.add_argument("pdf_file", help="Input PDF file to extract text from")
    parser.add_argument("--output", default="extracted_text.txt", help="Output text file name (default: extracted_text.txt)")
    parser.add_argument("--page", type=int, help="Specify a specific page number to extract")

    args = parser.parse_args()

    pdf_file = args.pdf_file
    output_text_file = args.output
    page_number = args.page

    extract_text(pdf_file, output_text_file, page_number)

if __name__ == "__main__":
    main()