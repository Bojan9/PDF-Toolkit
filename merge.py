import argparse
import PyPDF2
import os

def merge_pdfs(output_filename, input_files):
    merger = PyPDF2.PdfMerger()
    
    for file in input_files:
        merger.append(file)

    merger.write(output_filename)
    merger.close()

def main():
    parser = argparse.ArgumentParser(description="Merge PDF files.")
    parser.add_argument("output", help="Output PDF file name")
    parser.add_argument("inputs", nargs="+", help="Input PDF files to merge")
    
    args = parser.parse_args()
    
    output_filename = args.output
    input_files = args.inputs
    
    merge_pdfs(output_filename, input_files)
    
if __name__ == "__main__":
    main()
