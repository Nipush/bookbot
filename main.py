def main():
    book_path = "books/frankstein.txt"
    text = get_book_content(book_path)  # Read the book
    number_words = get_number_words(text)  # Count the number of words
    characters = get_number_characters(text)  # Count the number of characters
    letters = get_number_alphabet_characters(text)  # Count the number of alphabet characters
    print(f"The book has {number_words} words")
    print(f"The characters are:{characters}")
    print(letters)


def get_book_content(path: str) -> str:
    with open(path) as f:
        return f.read()
    

def get_number_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_number_characters(text: str) -> dict[str, int]:
    characters = {}
    for char in text.lower():
        if char.lower() in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters


def get_number_alphabet_characters(text: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    characters = {}
    result = ""

    for char in text.lower():
        if char in alphabet:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    for char in alphabet:
        if char in characters:
            result += f"The '{char}' character was found {characters[char]} times\n"
    
    return result

main()
