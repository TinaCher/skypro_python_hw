square_side_str = input("Side: ")

# Convert the input to a float first
square_side_float = float(square_side_str)

# Round up if the number is not an integer
if square_side_float != int(square_side_float):
    square_side = int(square_side_float) + 1
else:
    square_side = int(square_side_float)

# Calculate the square
square = square_side * square_side

print(square)


##Convert the input to a float: This ensures that even if the user inputs a decimal number, 
# it will be handled correctly. 
# Check if the number is an integer: We use int(square_side_float) to convert the float 
# to an integer. If square_side_float is not equal to this integer value, 
# it means the original number had a fractional part.
# Round up: If the number is not an integer, we add 1 to the integer part to round it up.
# Calculate the square: Finally, we calculate the square of the rounded-up value.
