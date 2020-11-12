from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
	""" Checks answer agains guess. Return the number of turns remaining."""
	if guess > answer:
		print("Too high")
		return turns - 1
	elif guess < answer:
		print("Too low")
		return turns - 1
	else:
		print(f"You got it! The answer was {answer}")


# Make function to set difficulty.
def set_difficulty():
	level = input("Choose a difficutly. Type 'easy' or 'hard': ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS


def game():
	# Choosing a random number between 1 and 100.
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	answer = randint(1, 100)
	print(f"Pssst, the correct answer is {answer}")

	turns = set_difficulty()
	guess = 0
	game_is_over = False
	while not game_is_over:
		print(f"You have {turns} attempts remaining to guess the number.")

		# Let the user guess a number.
		guess_is_a_number = False
		while not guess_is_a_number:
			try:
				guess = int(input("Make a guess:"))
				guess_is_a_number = True
			except ValueError:
				print("Please guess a number")

		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print(f"You've run out of guesses. You lose")
			game_is_over = True
		elif guess != answer:
			print("Guess again.")


game()
