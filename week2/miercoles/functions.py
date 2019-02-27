def greet():
    print("welcome")

# showing the memory location
print(greet) # <function greet at 0x10609e1e0>
print(id(greet)) # 4559856096

# = greet()
greet.__call__()
greet()


def greet(name, nickname):
    print(f"{name}, welcome {nickname}")

greet("caden", "caycay")

def describe_pet(animal_type, name="polly"):
    print(f"{name} is a {animal_type}")

describe_pet('cat', 'muzi')
describe_pet(name="polly", animal_type="parrot")

# *args takes in a list
def pet(name, *args):
    print(f"This is {name}.")
    print("more info:")
    for item in args:
        print(f"-{item}")

pet("woofi", "black", "lice", "barks")


def pet2(name, **kwargs): # keyword arguments
    print(f"This is {name}.")
    for k, v in kwargs.items():
        print(k + " maps to " + v)
    print(kwargs)

# passing the keywords to a function through **kwargs
pet2("woofi", color = 'black', parasite = 'lice', like_to_do = "barks" )


def whisper(text):
    up = text.upper()
    low = text.lower()
    return up, low
up, low = whisper("wHat's up?") # unpacking a tuple
print(up)
print(low)