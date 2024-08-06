import PyPDF2
import docx2txt


def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize a variable to store all the text
        full_text = ""
        
        # Iterate through each page in the PDF file
        for page in pdf_reader.pages:
            # Extract text from the page and add it to the full_text variable
            full_text += page.extract_text() + "\n"

    return full_text


def extract_text_from_docx(file):
    return docx2txt.process(file)


def extract_text_from_file(file):
    if file.type == "application/pdf":
        text = extract_text_from_pdf(file)
        return text
    elif (
        file.type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        text = extract_text_from_docx(file)
        return text
    elif file.type == "application/json":
        return file.getvalue().decode("utf-8")
    elif file.type == "application/txt":
        return file.getvalue().decode("utf-8")
    else:
        print("Error in the file format")




