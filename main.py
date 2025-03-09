from stats import get_num_words, get_num_chars

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    print(f"{word_count} words found in the document")
    print(f"{char_count}")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

if __name__ == '__main__':
    main()