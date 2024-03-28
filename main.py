def count_words(text):
    words = text.split()
    print(f"{words}")

def main():
    with open("books/frankenstein.txt") as file:
        text = file.read()
        count_words(text)
        
        
if __name__ == "__main__":
    main()