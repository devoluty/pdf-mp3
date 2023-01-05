import pdfplumber as pp
from gtts import gTTS
import re
import os


def create_text():
    route = "/home/mario/Documentos/books/el-gran-gatsby.pdf"

    with pp.open(route) as book:
        for page_no, page in enumerate(book.pages, start=1):
            data = page.extract_text()
            print(page_no)
            with open("gatsby.txt", "a") as reader:
                try:
                    reader.write(data.strip())
                finally:
                    reader.close()


def clean_txt():
    # Do what is necessary
    with open('gatsby.txt', 'r') as f:
        contents = f.read()

    contents = re.sub("COsta rICa", "", contents)

    with open('gatsby.txt', 'w') as f:
        f.write(contents)


def create_mp3(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    with open(input_file, 'r') as f:
        text = f.read()

    language = 'es'
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(output_file)
    print('speech.save function returned')


def main():
    #create_text()
    #clean_txt()
    create_mp3('gatsby.txt', 'gatsby.mp3')


if __name__ == "__main__":
    main()