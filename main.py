def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_word = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f'--- Begin report of {book_path} ---')
    print(f"{count_word} words found in the document")
    print()
    for i in chars_sorted_list: 
        if not i["char"].isalpha():    
            continue
        print(f"The '{i['char']}' character was not found {i['num']} times")
    print("---End report---")

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = [ ]
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key= sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}

    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()    

main()




