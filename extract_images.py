import argparse
import os
from PyPDF2 import PdfReader

def extract_images(pdf_file, output_folder, page_number=None):
    reader = PdfReader(pdf_file)

    # If a specific page number is not specified, extract images from all pages
    if page_number is not None:
        pages_to_process = [reader.pages[page_number - 1]]
    else:
        pages_to_process = reader.pages

    count = 0
    for page in pages_to_process:
        for image_file_object in page.images:
            image_data = image_file_object.data
            image_filename = os.path.join(output_folder, f"{count}_{image_file_object.name}")

            # Create the output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            with open(image_filename, "wb") as image_file:
                image_file.write(image_data)

            count += 1

    print(f"Images extracted from {pdf_file} (Page {page_number if page_number else 'All'}) and saved to {output_folder}")

def main():
    parser = argparse.ArgumentParser(description="Extract images from a PDF file and save them to a folder.")
    parser.add_argument("pdf_file", help="Input PDF file to extract images from")
    parser.add_argument("--output", default="extracted_images", help="Output folder for images (default: extracted_images)")
    parser.add_argument("--page", type=int, help="Specify a specific page number to extract")

    args = parser.parse_args()

    pdf_file = args.pdf_file
    output_folder = args.output
    page_number = args.page

    extract_images(pdf_file, output_folder, page_number)

if __name__ == "__main__":
    main()
