'''
This code generate a the code-review group for Python class.
1. 3 person a team of 4 teams, except one with only two persons.
2. ideal nobody has the same group-mates from previous week

Note: need to modify to take in previous weeks...
'''
import random


def unpack_list(nested_list, flat_list=[]):
    '''unpacking list function flattens a list of lists'''
    for item in nested_list:
        if type(item) == list:
            unpack_list(item)
        else:
            flat_list.append(item)
    return flat_list


s = ['andy', 'arno', 'ben', 'blake', 'casey', 'daniel', 'freddy', 'melissa', 'micheal', 'ming', 'nick', 'rob']
week0 = [["rob","ming","casey"], ["andy","melissa","arno"], ["ben","freddy","micheal"], ["blake","daniel","nick"]]
# week2 result:
week1 = [["rob","melissa","daniel"], ["ming","arno","ben"], ["casey","freddy","andy"], ["blake","micheal","nick"]]
# week 3 = result:
week3 = [['rob', 'andy', 'arno'], ['melissa', 'freddy', 'blake'], ['daniel', 'casey', 'ben'], ['nick', 'ming', 'micheal']]
group_1, group_2, group_3, group_4 = [], [], [], []

counter=0
first_choice = 0
second_choice = 2
third_choice = 1
fourth_choice = 3

# starting from splitting up first choice to group 1 to 3
for i in week1[first_choice]:
    counter += 1 # look through the list one by one
    eval("group_" + str(counter)).append(i) # start creating group 1

# flattening third and fourth_choice into a new list: leftover
leftover = []
for i in range(3):
    leftover.append(week1[third_choice][i])
for i in range(3):
    leftover.append(week1[fourth_choice][i])

# start the fourth group by one random person from leftover
x = random.choice(leftover)
eval("group_" + str(4)).append(x)
leftover.remove(x)

counter=0
random.shuffle(week1[second_choice])
# splitting second_choice and filling to group1 to 3
for i in week1[second_choice]:
    counter += 1
    eval("group_" + str(counter)).append(i)

# filling the fourth group by one random person from leftover
y = random.choice(leftover)
eval("group_" + str(4)).append(y)
leftover.remove(y)

counter = 0
random.shuffle(leftover)
for i in leftover:
    counter += 1
    eval("group_" + str(counter)).append(i)

print(group_1, group_2, group_3, group_4)
