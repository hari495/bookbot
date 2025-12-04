from stats import get_book_length, count_chars, sort_dicts
import sys
def get_book_text(path):    
    with open(path) as f:
        return f.read()


def main():
    try:
        file_path=sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(file_path)
    num_words=get_book_length(text)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...")
    print(f"Found {num_words} total words")

    char_dict=count_chars(text)
    sorted=sort_dicts(char_dict)

    print("--------- Character Count -------") 
    
    for pair in sorted:
        char=pair["char"]
        if char.isalpha():
            print(f"{char}: {pair["num"]}")
    
    print("============= END ===============")



main()

