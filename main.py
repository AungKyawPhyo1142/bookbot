import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    file_path = sys.argv[1] 
    
    book_content = get_book_text(file_path)
    num_words = count_words(book_content)
    characters = count_characters(book_content)
    # convert characters dict into list
    characters = [{"char": char, "num": num} for char, num in characters.items()]
    sort_characters(characters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in characters:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()