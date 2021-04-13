# nesting a for loop
letters = ['a', 'b', 'c', 'd']
num = [1, 2, 3, 4]
for x in letters:
    for y in num:
        print(str(x) + ' is to ' + str(y))

# All available groups here
output = [' finance ', ' management ', ' hr ', ' legal ', ' sales ']


# User's prefered groups
chosenGroups = [' hr ', ' legal ', ' IT ']

for a in output:
    for b in chosenGroups:
        if b == a:
            found = True
            print('This is an existing group' + b)

            found = False
        print('This is not an existing group' + a)