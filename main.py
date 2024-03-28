def main():
    book_path: str = "books/frankenstein.txt"
    text: str = get_book_text(book_path)
    num_words: int = get_count_words(text)
    letter_count: dict = get_count_letters(text)
    print_report(num_words, letter_count, book_path)

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

def print_report(num_words, letter_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    
    
        
        
if __name__ == "__main__":
    main()