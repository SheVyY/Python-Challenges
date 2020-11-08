import random

print("Who's paying today?")
print("We will find out!")

# Store the names of the paying people
nameAsCSV = input("Give me everybody's names: ")
names = nameAsCSV.split(", ")
print(names)

# Get the total number of items in a list.
num_items = len(names)
# Generate random number between 0 and the last index of the list
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today")





