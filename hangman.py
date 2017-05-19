

# The user needs to be able to input letter guesses.

# A limit should also be set on how many guesses they can use. T


# his means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list.



#  You will also need functions to check if the
# user has actually inputted a single letter,

#  	 to check if the inputted letter is in the hidden
# word (and if it is, how many times it appears),

#  	 to print letters, and a counter variable to limit guesses.

#  generate a random word

#
import random

hangman_list = ['patriots', 'revolution', 'athenahealth', 'franklin']
count = 0

def main():
	# generate_random_word()
	user_guess()


def generate_random_word(word_list):
	word = random.choice(word_list)
	return word


def user_guess():

	text = input('What letter would you like to choose: ')
	word = generate_random_word(hangman_list)
	print(word)

	# need verification that string is a valid letter
	while len(text) != 1 and text != str(text):

		if len(text) != 1 and text == str(text):
			text = input('Try again, it was not 1 letter: ')

		elif len(text) == 1 and text != str(text):
			text = input('You did not print a string, try again: ')

		else:
			text = input('Please choose a letter: ')

	text = text.lower()


	check_guess_with_word(text, word)


def check_guess_with_word(text, word):

	word = list(word)
	for k,c in word.items():


	print(text + ' ' + word[0])



if __name__ == '__main__':
	main()
