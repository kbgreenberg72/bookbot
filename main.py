def get_count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_count_words(text)
    print(f"{num_words} words found in the document")
        
        
if __name__ == "__main__":
    main()