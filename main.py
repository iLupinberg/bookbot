def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_book_word_count(text)
    char_dict = get_book_character_count(text)
    char_dict_sorted = sorted(char_dict.items(), reverse=True, key=lambda p: p[1])
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for n in char_dict_sorted:
        if n[0].isalpha() == True:
            print(f"The {n[0]} character was found {n[1]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_word_count(path):
    words = path.split()
    return len(words)

def get_book_character_count(path):
    dict = {}
    for char in path:
        char = char.lower()
        if char not in dict:
            dict[char] = 1
        elif char in dict:
            dict[char] += 1
    return dict

def sort_on(dict):
    return dict[values]

main()