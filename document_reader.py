import fitz  # PyMuPDF
import docx
from io import StringIO

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = [paragraph.text for paragraph in doc.paragraphs]
    return "\n".join(text)

def read_txt(file):
    text = file.read().decode("utf-8")
    return text

def read_document(file):
    if file.name.endswith(".pdf"):
        return read_pdf(file)
    elif file.name.endswith(".docx"):
        return read_docx(file)
    elif file.name.endswith(".txt"):
        return read_txt(file)
    else:
        raise ValueError("Unsupported file type")
