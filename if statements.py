'''
An if statement chooses where to go based on a boolean expression.
True and True is a boolean expression.
'''

b1 = True
b2 = False

if b1 and b2:
    print('Both b1 and b2 are True')
elif b1 and not b2:
    print('B1 is True, but b2 is False')
elif not b1 and b2:
    print('B1 is False, but b2 is True')
else:
    print('Both b1 and b2 are False')

# Most of the time, you should be ending an if statement with an else.

string = '102'

if string == '102':
    print(True)

if string == 102:
    print(True)
    # This will not print, as '102' is not 102

if int(string) == 102:
    print(True)
    # This will print

# And will only be True if all of the arguments connected by ands are True
# Or will be True if any of the arguments connected by ors are True.
# == means is equal to. = is assigning a value to a variable.

# if b1 and b2 means the same thing as if b1==True and b2==True
