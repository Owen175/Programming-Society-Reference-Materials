# String to integer:
string = '123'
num = int(string)
print(num)

string = '12f'
num = int(string)
# This will cause an error. f cannot be converted to an integer

# Any to string:
num = 1.23
string = str(num)
print(string)

# You don't generally convert from list to anything else, or anything else to list.



