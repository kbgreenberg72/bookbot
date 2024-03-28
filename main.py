def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_count_words(text)
    print(f"{num_words} words found in the document")
    letter_count = get_count_letters(text)
    print(f"Letter count:\n {letter_count}")

def get_count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_count_letters(text):
    lowercase_text = text.lower()
    letter_count = {}
    for char in lowercase_text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count
        
        
if __name__ == "__main__":
    main()