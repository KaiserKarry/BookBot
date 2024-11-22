def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = number_of_words(book_text)
    letter_count = number_of_letters(book_text)
    seperate_letter_dictionaries(letter_count)
    # print(letter_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_letters(text):
    # convert text to all lowercase
    lowered_text = text.lower()

    # make empty dictionary to populate
    letters = {}

    # iterate over each character checking if its in the dictionary or not. If it is then raise the count by 1, if it isnt then add an entry.
    for character in lowered_text:
        if character in letters:
            letters[character] += 1
        else:
            letters[character] = 1
    return letters

def seperate_letter_dictionaries(text):
    # empty list
    seperated_list = []

    # iterating over every entry in the text dictionary and adding it seperately to the list
    for i in text:
        if i.isalpha():
            seperated_list += i
            print (f"key is {i}, value is {text[i]}")
        else:
            pass
    return seperated_list


main()