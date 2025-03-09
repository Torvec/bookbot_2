def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    char_count = {}
    for text in book_text:
        lower_text = text.lower()
        if lower_text.isalpha():
            if lower_text in char_count:
                char_count[lower_text] += 1
            else:
                char_count[lower_text] = 1
    return char_count
