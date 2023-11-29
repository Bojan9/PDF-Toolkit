from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import argparse

def convert_txt_to_pdf(input_txt, output_pdf):
    # Read the content from the text file
    with open(input_txt, 'r', encoding='utf-8') as txt_file:
        text_content = txt_file.read()

    # Create a PDF file and add text to it
    pdf_canvas = canvas.Canvas(output_pdf, pagesize=letter)
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(100, 700, text_content)

    # Save the PDF file
    pdf_canvas.save()

    print(f"Conversion was completed. PDF saved to {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Convert a text file to a PDF file.")
    parser.add_argument("input_txt", help="Input text file to convert")
    parser.add_argument("output_pdf", help="Output PDF file name")

    args = parser.parse_args()

    input_txt = args.input_txt
    output_pdf = args.output_pdf

    convert_txt_to_pdf(input_txt, output_pdf)

if __name__ == "__main__":
    main()
