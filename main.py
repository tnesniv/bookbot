from stats import word_count

def main():
    path_frankenstein = "books/frankenstein.txt"
    text_frankenstein = get_book_text(path_frankenstein)
    print(f"{word_count(text_frankenstein)} words found in the document")

# Open a file and output the raw text; close the file
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

main()
