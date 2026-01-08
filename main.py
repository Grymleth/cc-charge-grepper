import pymupdf
from pprint import pprint
from os import listdir

FILES_PATH = "./files"

def _output_text(word_stream: list[str]):
    for word in word_stream:
        print(word)

def _get_all_files():
    return listdir(FILES_PATH)

def _extract_words(filename: str):
    doc = pymupdf.open(f"{FILES_PATH}/{filename}")
    words_in_page = []
    for page in doc:
        text = _clean_text(page.get_text("text"))
        words = text.split("\n")
        words_in_page.extend(words)
    return words_in_page

def _clean_text(text: str):
    text = text.replace(" ", "")
    return text
    

def main():
    files = _get_all_files()
    
    word_stream = []
    for filename in files:
        extracted_words = _extract_words(filename)
        word_stream.extend(extracted_words)
        
    _output_text(word_stream)
    
if __name__ == "__main__":
    main()