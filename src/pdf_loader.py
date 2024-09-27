#load pdf and break it into text with respective page numbers
from data import test
import PyPDF2


def extract_pages(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(reader.numPages)
        for page_num in range((reader.numPages)):
            page_text = reader.pages[page_num].extract_text()
            yield page_num + 1, page_text
 

