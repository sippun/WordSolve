import sys
from itertools import chain, permutations

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
	if len(sys.argv) == 2:
		START_LEN = 3

		#Sort the starting letters
		letters = ''.join(sorted(sys.argv[1]))

		perms = chain.from_iterable(permutations(letters, r) for r in range(START_LEN, len(letters)+1))
		word_opts = list(map(''.join, perms))

    	english_words = load_words()

    	for word in word_opts:
    		if word in english_words:
    			print(word)
