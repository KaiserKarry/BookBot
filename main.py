def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = number_of_words(book_text)
    letter_count = number_of_letters(book_text)
    letter_dictionaries_list = seperate_letter_dictionaries(letter_count)
    letter_dictionaries_list.sort(reverse=True, key=sort_on)
    print_loop(letter_dictionaries_list, word_count)

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
    seperated_list = []

    # iterating over every entry in the text dictionary and adding it seperately to the list if it is a alpha.
    for i in text:
        if i.isalpha():
            individual_entry = {}
            individual_entry["letter"] = i 
            individual_entry["number"] = text[i]
            seperated_list.append(individual_entry)
        else:
            pass
    return seperated_list

def sort_on(dict):
    return dict["number"]

# function to print the desired stats for frankenstein. Havent learnt about user input yet.
def print_loop(dict, word_count):
    print("------- Begin Report --------")
    print(f"{word_count} words were found in the book of Frankenstein")
    for i in dict:
        print(f"The '{i["letter"]}' character was found {i["number"]} times.")
    print("--- End Report ---")
main()