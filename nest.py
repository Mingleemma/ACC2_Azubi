# letters = ['a', 'b']
# num = [1, 2, 3, 4, 5, 7, 5]
# for x in letters:
#     for y in num:
#         print (str(x) + ' is to ' + str(y))

#All available groups on the system
output = ['finance', 'management', 'hr', 'legal', 'sales']

#User's preferred groups
chosengroups = ['hr', 'legal', 'it']

for a in output:
    for b in chosengroups:
        if b == a:
            found = True
            print('This is an existing group ' + b)
    #     else:
    #         found = False
    # print('This is not an existing group' + a)