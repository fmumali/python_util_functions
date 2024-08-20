from PyPDF2 import PdfReader, PdfWriter

import os

def merge_pdfs(input_folder, output_folder, output_filename):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create a PdfWriter object for writing the merged PDF
    pdf_writer = PdfWriter()

    # Get all PDF files in the input folder and sort them numerically by filename
    input_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
    sorted_files = sorted(input_files, key=lambda x: int(x.split('.')[0]))

    # Loop through all sorted PDF files in the input folder
    for file_name in sorted_files:
        pdf_path = os.path.join(input_folder, file_name)
        pdf_reader = PdfReader(pdf_path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF to the output folder
    output_path = os.path.join(output_folder, output_filename)
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Example usage
input_folder = './input'
output_folder = './output'
output_filename = 'filename.pdf'
merge_pdfs(input_folder, output_folder, output_filename)

print("Merging completed. The merged file is saved as:", output_filename)