import os
import PyPDF2

def extract_text_from_pdf(input_pdf_path, output_dir):
    """
    Necessary pip install PyPDF2==2.11.1

    :param input_pdf_path: The path to the input PDF file.
    :param output_dir: The directory where the output text files will be saved.
    """
    # Open the input PDF file in read-binary mode
    with open(input_pdf_path, 'rb') as input_pdf:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfFileReader(input_pdf)

        # Create a new directory for the output text files
        os.makedirs(output_dir, exist_ok=True)

        # Loop through each page in the PDF file
        for page_num in range(pdf_reader.numPages):

            # Extract text from the current page
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Create a new text file with the page number as the filename
            with open(f"{output_dir}/{filename}_{page_num}.txt", 'w') as output_txt:
                # Write the extracted text to the output text file
                output_txt.write(text)

# Example usage
input_pdf_path = input("Insert path to PDF file: ")
output_dir = os.path.splitext(input_pdf_path)[0]

# Call the extract_text_from_pdf function for the current PDF file
extract_text_from_pdf(input_pdf_path, output_dir)