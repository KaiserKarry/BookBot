def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = number_of_words(book_text)
    print(word_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    return len(words)

main()