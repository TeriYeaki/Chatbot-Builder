import PyPDF2

def extract_text_from_pdf(pdf_path):

    """Extract text from pdf file using PyPDF2 library."""

    text = ""

    with open(pdf_path, 'rb') as file:

        pdf_reader = PyPDF2.PdfReader(file)

        for page in range(len(pdf_reader.pages)):

            text += pdf_reader.pages[page].extract_text()

    return text
