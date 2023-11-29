# PDF Toolkit

This repository contains a set of Python scripts for working with PDF files. Each script serves a specific purpose related to PDF manipulation. The scripts use the [PyPDF2 library](https://pypdf2.readthedocs.io/en/3.0.0/index.html).

## Installation

```bash
# Install the required library
pip install PyPDF2

# For extracting the images
pip install PyPDF2[image]

# Or just install all optional dependencies
pip install PyPDF2[full]
```

## Scripts Overview

### 1. merge.py

This script merges multiple PDF files into a single PDF file.

#### Usage:

```bash
# Run the script
python merge.py output.pdf input1.pdf input2.pdf input3.pdf
```

### 2. extract_text.py

This script extracts text from PDF files, either from all pages or a specific page.

#### Usage:

```bash
# Extract text from all pages
python extract_text.py file.pdf --output text_file.txt

# Extract text from page 3
python extract_text.py file.pdf --output text_file.txt --page 3
```

### 3. extract_images.py

This script extracts images from PDF files, either from all pages or a specific page.

#### Usage:

```bash
# Extract images from all pages to the default folder "extracted_images"
python extract_images.py example.pdf

# Extract images from page 2 to a custom folder "my_images"
python extract_images.py example.pdf --output my_images --page 2
```

### 4. extract_pages.py

This script creates a new PDF file from specific pages of an existing PDF.

#### Usage:

```bash
# Create a new PDF file containing pages 3, 4, and 7
python extract_pages.py input.pdf output.pdf 3 4 7

# Create a new PDF file containing pages 1 and 2
python extract_pages.py input.pdf output.pdf 1 2
```

### 5. split_pdf.py

This script splits every page of a PDF file and stores them in a new folder.

#### Usage:

```bash
# Split input.pdf into individual pages in the default folder "split_pages"
python split.py input.pdf

# Split input.pdf into individual pages in a custom folder "output_folder"
python split.py input.pdf --output output_folder
```

### 6. compare.py

This script compares the text content of corresponding pages in two PDF files. If differences are found, it prints the differing text for each page.

#### Usage:

```bash
# Compare two PDF files and save differences to differences.txt
python compare.py file1.pdf file2.pdf --output differences.txt
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/Bojan9/PDF-Toolkit.git
cd pdf-toolkit
```

2. Navigate to the directory of the script you want to use.

3. Follow the usage instructions provided above for each script.
