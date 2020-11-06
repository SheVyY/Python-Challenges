# Print the starting map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# Ask for coordinates
position = (input("Where do you want to put the treasure? Type coordinates horizontal[1-3] vertical[1-3]:\n "))

# Extract the position for coordinates
horizontal = int(position[0])
vertical = int(position[1])

# Find the exact spot on the map and place "X"
map[vertical - 1][horizontal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
