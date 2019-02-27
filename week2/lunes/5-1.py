'''
5-1. Conditional Tests: Write a series of conditional tests .
 Print a statement describing each test and your prediction for the results of each test .
 Your code should look something like this:
                  car = 'subaru'
                  print("Is car == 'subaru'? I predict True.")
                  print(car == 'subaru')
                  print("\nIs car == 'audi'? I predict False.")
                  print(car == 'audi')
• Look closely at your results, and make sure you understand why each line evaluates to True or False .
• Create at least 10 tests . Have at least 5 tests evaluate to True and another 5 tests evaluate to False .
'''
x = 2
cube = x ** 3
y = -8
cube == 8
print("Is cube = 8? I predict True.")
print(cube == 8)

print("Is cube = 8.00? I predict True.")
print(cube == 8.00)

print("Is cube = 6? I predict False.")
print(cube == 6)

print("Is cube = '8'? I predict False.")
print(cube == '8')

print("Is cube != -y ? I predict False.")
print(cube != -y)

print("Is 12 % 5 == x? I predict True.")
print(12 % 5 == x)

print("Is (True == False or 1 == True) == True? I predict True.")
print((True == False or 1 == True) == True)

print("Is (1 == False and 1 == True) == True? I predict False.")
print((1 == False and 1 == True) == True)

print("Is -12 % 5 == -2 ? I predict False.")
print( -12 % 5 == -2)

print("Is -12 % 5 == 3 ? I predict True.")
print( -12 % 5 == 3)

print("Is  False >= True ? I predict False.")
print( False >= True)

print("Is  _ >= True ? I predict an error message.")
print( _ >= True)
