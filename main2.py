import os
import PyPDF2

def split_pdf_into_pages(input_pdf_path, output_dir):
    """
    Necesario pip install PyPDF2==2.11.1  
    

    :param input_pdf_path: The path to the input PDF file.
    :param output_dir: The directory where the output PDF files will be saved.
    """
    # Open the input PDF file in read-binary mode
    with open(input_pdf_path, 'rb') as input_pdf:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfFileReader(input_pdf)

        # Create a new directory for the output PDF files
        os.makedirs(output_dir, exist_ok=True)

        # Loop through each page in the PDF file
        for page_num in range(pdf_reader.numPages):

            # Create a new PDF file with the page number as the filename
            with open(f"{output_dir}/{filename}_{page_num}.pdf", 'wb') as output_pdf:
                # Create a new PDF file writer object
                pdf_writer = PyPDF2.PdfFileWriter()

                # Add the current page to the PDF file writer object
                pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Write the PDF file writer object to the output PDF file
                pdf_writer.write(output_pdf)

                

# Example usage
input_pdf_dir = input ("Insert path ") # r'C:\Users\franc\Projects\PDF\PDF-OTF'

# Loop through each PDF file in the input directory
for input_pdf_path in os.listdir(input_pdf_dir):
    if input_pdf_path.endswith('.pdf'):

        filename = input_pdf_path

        # Create a new directory for the output PDF files
        output_dir = os.path.join(input_pdf_dir, input_pdf_path[:-4])
        os.makedirs(output_dir, exist_ok=True)

        # Call the split_pdf_into_pages function for the current PDF file
        split_pdf_into_pages(os.path.join(input_pdf_dir, input_pdf_path), output_dir)