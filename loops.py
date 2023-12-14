# Loops

# While loops
# While loops repeat whilst a condition is True
cont = True
string = ''
while cont:
    string += '_' # Adds _ to the end of the string
    if len(string) > 5:  # Checks if the length of the string is longer than 5
        cont = False

# This will loop until the string has 6 underscores
# A while loop's condition can be as long as you want.


# For loops:
for i in range(10):
    print(i)
    # This will print: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (NOT 10)
# The function range() makes a range from 0 to the number-1.


ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for l in ls:
    print(l)
    # Prints every item in the ls in turn
    # Also prints from 0 to 9
