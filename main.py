def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    letters_dict =  get_letters_dict(text)
    letters_sort_list = letters_dict_to_sorted_list(letters_dict)
    print(f"--- Book report of {book_path} ---")
    print(f"{num_words} words found in {book_path}")
    print()

    for item in letters_sort_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def letters_dict_to_sorted_list(num_letters_dict):
    sorted_list = []
    for let in num_letters_dict:
        sorted_list.append({"char": let, "num": num_letters_dict[let]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letters_dict(text):
    letters = {}
    for l in text:
        lowered = l.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()