
def get_num_words(text):
        return len(text.split())

def get_num_chars(text):
	letters = {}
	lower_cases = text.lower()
	for lower_case in lower_cases:
		if lower_case in letters:
			letters[lower_case] += 1
		else:
			letters[lower_case] = 1
	return letters


def sort_dict(letters):
	letter_list = []
	for character, count in letters.items():
		letter_dict = {}
		letter_dict.update({"char": character, "num": count})
		letter_list.append(letter_dict)
	def sort_on(items):
		return items["num"]
	letter_list.sort(reverse=True, key=sort_on)
	return letter_list
	






