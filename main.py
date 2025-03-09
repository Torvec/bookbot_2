import sys
from stats import get_num_words, get_num_chars, list_char_counts, sort_list

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    char_count_list = list_char_counts(char_count)
    sorted_char_count_list = sorted(char_count_list, reverse=True, key=sort_list)
    report = print_report(sorted_char_count_list)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(report)
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def print_report(sorted_list):    
    report = ""
    for char in sorted_list:
        letter = char["letter"]
        count = char["count"]
        report += f"{letter}: {count}\n"
    return report

if __name__ == '__main__':
    main()