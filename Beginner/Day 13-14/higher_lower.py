from art import logo, vs
from game_data import data
import random


def format_data(account: dict) -> str:
	"""Format the account data into printable format"""
	account_name = account["name"]
	account_description = account["description"]
	account_country = account["country"]
	return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess: str, a_followers: int, b_followers: int) -> bool:
	"""Take the user guess and follower counts and returns if they got it right"""
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"

# Print the game logo
print(logo)
# Set the begging score to 0
score = 0
# While loop flag
game_should_continue = True
# Define and generate the account before the loop so it can switch after
account_b = random.choice(data)

# Play the guessing game until the user is wrong
while game_should_continue:

	# Making account at position B become the next account at position A
	account_a = account_b
	account_b = random.choice(data)

	# Generate new account if they're both equal
	account_a = random.choice(data)
	if account_a == account_b:
		account_b = random.choice(data)

	# Print compare statements for both accounts
	print(f"Compare A: {format_data(account_a)}")
	print(vs)
	print(f"Compare B: {format_data(account_b)}")

	# Ask the user, what account has more followers
	guess = input("Who has mor followers? Type 'A' or 'B': ").lower()

	# Find the number of followers for both accounts
	a_follower_count = account_a["follower_count"]
	b_follower_count = account_b["follower_count"]

	# Call the function that checks the number of followers and assign it to the variable
	is_correct = check_answer(guess, a_follower_count, b_follower_count)

	# Give user feedback on their guess
	if is_correct:
		score += 1
		print(f"You're right! Current score: {score}")
	else:
		game_should_continue = False
		print(f"Sorry, that's wrong. Final score: {score}")
