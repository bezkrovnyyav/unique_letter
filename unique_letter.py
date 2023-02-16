from collections import Counter


def get_one_unique_letter(text):
	def get_first_unique_letter(word):
		for letter, quantity in Counter(word).items():
			if quantity == 1:
				return letter

	words = text.split(" ")
	list_enique_char = []

	for word in words:
		list_enique_char.append(get_first_unique_letter(word))
	return get_first_unique_letter(list_enique_char)


if __name__ == '__main__':
   text = '''C makes it easy for you to shoot yourself in the foot.
   C++ makes that harder, but when you do, it blows away your whole leg.
                                                   (с) Bjarne Stroustrup
'''
   print(f"The unique lette is: {get_one_unique_letter(text)}")
