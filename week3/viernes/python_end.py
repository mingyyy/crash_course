# enumerate
my_list = [1,2,3,84,43]
location =["IND", "ESP", "CHN", "MEX"]

for index, value in enumerate(my_list, start=100):
    print(f"at {index} lives {value}")

for index, value in enumerate(location, start=1):
    print(f"{index}. {value}")
    # print(location.index(value))

# list comprehension
new_list1 = [i+1 for i in my_list if not i % 2 == 0]
# doing the same thing
new_list2 = []
for i in my_list:
    if not i% 2 == 0:
        new_list2.append(i+1)

print(new_list1)
print(new_list2)

# generator expressions
new_li = [x+1 for x in my_list]
print(new_li)

gen = (x+1 for x in my_list)
print(gen) # <generator object <genexpr> at 0x109800cf0>
# getting the same logic but not the end result, much smaller storage
# a iterable object; the generator only create the value on the fly.

for x in gen:
    print(x)


# lambda expression: anonymous function
def square(x):
    return x ** 2


print(square(2))

# lambda x : f(x)
# sq = lambda x, y: (x+y)**2
sq = lambda x: True if x % 2 == 0 else False
print(sq(2))
print(sq(3))

# map takes in a function and then an iterable
squared_lam = list(map(lambda x: x**2, my_list))
squared_def = list(map(square, my_list))
print(squared_lam == squared_def)


# positional argument, optional argument, any length argument
def my_funct(name, age = 13, *args, **kwargs):
    print(name)
    print(args[-1])
    for item in args:
        print(item)

my_funct("martin", 5, 4, "hello","etc.")

def fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} maps to {value}.")

fun(name = "martin", number = 1, greeting = "hello")

