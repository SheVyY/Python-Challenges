student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

# Calculates average without using sum() or len() functions
number_of_students = 0

for student in student_heights:
	number_of_students += 1

total_height = 0

for height in student_heights:
	total_height += height


# Average students height
average_height = round(total_height / number_of_students)
print(f"Average students hight is {average_height}cm")
