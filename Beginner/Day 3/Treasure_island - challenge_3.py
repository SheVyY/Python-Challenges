print()
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("-" * 40)

choice_1 = input('Where do you want to go? Type "left"" or "right": \n').lower()
if choice_1 == "left":
	print("You've moved over the trap without a problem and you go further")
	choice_2 = input(
		'You\'ve are close by a very fast running river, do you wanna swim over or wait? Type "swim"" or "wait" \n').lower()
	if choice_2 == "wait":
		print("Great choice, you waited and now you can safely go across the river")
		print("You've reach a mysterious crossroad and you're starring at 3 doors")
		choice_3 = input('You choose "red", "yellow" or "blue" doors? \n ').lower()
		if choice_3 == "yellow":
			print('''
			*******************************************************************************
			          |                   |                  |                     |
			 _________|________________.=""_;=.______________|_____________________|_______
			|                   |  ,-"_,=""     `"=.|                  |
			|___________________|__"=._o`"-._        `"=.______________|___________________
			          |                `"=._o`"=._      _`"=._                     |
			 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
			|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
			|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
			          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
			 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
			|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
			|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
			____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
			/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
			____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
			/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
			____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
			/______/______/______/______/______/______/______/______/______/______/_____ /
			*******************************************************************************
			''')
			print("Amazing, you've found a treasure")
			print("YOU'VE WON THE GAME ")
		elif choice_3 == "red":
			print("The doors shut behind you and the flames suddenly burned you to the death")
			print("Game over")
		elif choice_3 == "blue":
			print("Out of the thin air the beast is standing right in front of you")
			print("You've been murdered")
			print("Game over")
		else:
			print("No matter what you did, you can't get of the island and died of the old age")
	else:
		print("You've been attacked by an alligator")
		print("You lost your leg and bleed to death")
		print("Game over")
else:
	print("Oh no, you've fallen into the hole")
	print("Sorry, but the game is over")
