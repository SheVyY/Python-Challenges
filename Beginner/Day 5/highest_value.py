student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)

# Finding out the highest number
highest_number = 0

for number in student_scores:
	if number > highest_number:
		highest_number = number

print(f"The highest score is {highest_number}")

# Finding out the lowest number
lowest_number = highest_number

for number in student_scores:
	if number < lowest_number:
		lowest_number = number

print(f"The lowest score is {lowest_number}")
