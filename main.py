import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict

def main():
	if  len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	else:
		book_path = sys.argv[1]
		text = get_book_text(book_path)
		num_words = get_num_words(text)
		letters = get_num_chars(text)
		letters_sorted = sort_dict(letters)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {book_path}...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for dict in letters_sorted:
			character = dict["char"]
			count = dict["num"]
			if character.isalpha() is True:
				print(f"{character}: {count}")
		print("============= END ===============")



if __name__ == "__main__":
	main()
