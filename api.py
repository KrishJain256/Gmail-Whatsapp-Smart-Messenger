from dotenv import load_dotenv
load_dotenv()

# importing required classes
from pypdf import PdfReader
import glob


def embed_query(query):
    str1 = ""
    files = glob.glob("Files/*.pdf")

    for file in files:
        # creating a pdf reader object
        reader = PdfReader(file)

        pages = reader.pages
        for page in pages:
            text = page.extract_text()
            str1 += text
        str1 += "\n"

    return f"Referring to the text:\n{str1}\nAnswer the query:\n{query}"
