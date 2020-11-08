import random
from hangman_words import word_list
from hangman_art import logo, stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for i in range(word_length):
	display.append("_")

end_of_game = False
lives = 6

print(logo)

while not end_of_game:
	# Asks user to pick a letter
	guess = input("Guess a letter: ").lower()

	# Informs user if uses the same letter
	if guess in display:
		print(f"You've already guessed {guess}")

	# Check guessed letter
	for position in range(word_length):
		letter = chosen_word[position]
		if letter == guess:
			display[position] = letter

	# Player lose a live when the letter is not in the chosen_word
	if guess not in chosen_word:
		print(f"You guessed {guess}, that's not in the word. You have {lives - 1} lives left.")
		print()
		lives -= 1
		if lives == 0:
			end_of_game = True
			print("You lost")

	print(f"{' '.join(display)}")

	# Check if there are any blank positions
	if "_" not in display:
		end_of_game = True
		print("You won")

	# prints the corresponding stage based on our lives
	print(stages[lives])