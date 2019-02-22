'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive .
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers .
     (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .)
4-5. Summing a Million: Make a list of the numbers from one to one million,
     and then use min() and max() to make sure your list actually starts at one and ends at one million .
     Also, use the sum() function to see how quickly Python can add a million numbers .
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 .
     Use a for loop to print each number .
4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list .
4-8. Cubes: A number raised to the third power is called a cube .
     For example, the cube of 2 is written as 2**3 in Python . Make a list of the first 10 cubes
     (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube .
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .
'''
import time

# 4-3
for i in range(20):
    print(i+1, end=" ")

# 4-4
million = []
for i in range(1000000):
    million.append(i+1)
# show the start and the end 5 numbers of the list
print(million[:5])
print(million[-5:])

# 4-5
print(min(million), max(million))
start=time.time()
print(sum(million))
print(f"{round(time.time() - start, 5)} seconds used to add a million.")

# 4-6
for i in range(1,21,2):
    print(i, end=" ")

# 4-7
three = []
for n in range(10):
    three.append((n+1)*3)
print("")
for i in three:
    print(i, end=" ")

# 4-8
print("")
for i in range(11):
    print((i+1) ** 3, end=" ")

# 4-9 list comprehension
print("")
x = [(i+1)**3 for i in range(11)]
for i in x:
    print(i, end=" ")