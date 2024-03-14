import PyPDF2

def split_pdf_into_pages(input_pdf_path, output_dir):

    # Open the input PDF file in read-binary mode
    with open(input_pdf_path, 'rb') as input_pdf:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfFileReader(input_pdf)

        # Loop through each page in the PDF file
        for page_num in range(pdf_reader.numPages):
            # Create a new PDF file with the page number as the filename
            with open(f"{output_dir}/page_{page_num}.pdf", 'wb') as output_pdf:
                # Create a new PDF file writer object
                pdf_writer = PyPDF2.PdfFileWriter()

                # Add the current page to the PDF file writer object
                pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Write the PDF file writer object to the output PDF file
                pdf_writer.write(output_pdf)

# Example usage
input_pdf_path = 'OCR_Legal.pdf'
output_dir = 'output'

split_pdf_into_pages(input_pdf_path, output_dir)