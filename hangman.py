import random

hangman_list = ['patriots', 'revolution', 'celtics', 'bruins']

def main():
	play_the_game()


def play_the_game():
	max_guesses = 7
	guesses = ''

	hidden_word = generate_random_word(hangman_list)
	print(hidden_word)

	while max_guesses > 0:
		fail = 0

		# iterate over the hidden word
		for c in hidden_word:

			# if the letter is in the user's guess
			if c in guesses:
				print(c)
			else:
				print('_')
				fail += 1

		if fail == 0:
			print('you won!')
			break

		user_input = input("Pick a letter to guess: ")

		guesses += user_input

		if user_input not in hidden_word:
			print('Sorry,{} is not in the word'.format(user_input))
			max_guesses -= 1


def generate_random_word(word):
	return random.choice(word)

if __name__ == '__main__':
	main()
