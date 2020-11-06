print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?  in CZK "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
number_of_people = int(input("How many people to split the bill? "))
person_bill = (total_bill * (1 + tip)) / number_of_people
print(f"Each person should pay: {person_bill:.2f}")

