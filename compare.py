import argparse
from PyPDF2 import PdfReader

def compare_pdfs(file1, file2, output_file):
    reader1 = PdfReader(file1)
    reader2 = PdfReader(file2)

    # Check if the number of pages is the same in both PDFs
    if len(reader1.pages) != len(reader2.pages):
        print("PDFs have different numbers of pages. Cannot compare.")
        return

    with open(output_file, 'w', encoding='utf-8') as output:
        # Iterate through each page and compare the text content
        for page_num, (page1, page2) in enumerate(zip(reader1.pages, reader2.pages), 1):
            text1 = page1.extract_text()
            text2 = page2.extract_text()

            if text1 != text2:
                output.write(f"Differences found on page {page_num}:\n")
                output.write(f"Text in {file1} (Page {page_num}):\n{text1}\n\n")
                output.write(f"Text in {file2} (Page {page_num}):\n{text2}\n\n")
                output.write("="*40 + "\n\n")

    print(f"Comparison completed. Differences saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Compare two PDF files and save differences to a text file.")
    parser.add_argument("file1", help="First PDF file for comparison")
    parser.add_argument("file2", help="Second PDF file for comparison")
    parser.add_argument("--output", default="differences.txt", help="Output text file to save differences (default: differences.txt)")

    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2
    output_file = args.output

    compare_pdfs(file1, file2, output_file)

if __name__ == "__main__":
    main()
