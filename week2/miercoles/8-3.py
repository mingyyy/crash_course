'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message
that should be printed on the shirt .
The function should print a sentence summarizing the size of the shirt and the message printed on it .
Call the function once using positional arguments to make a shirt .
Call the function a second time using keyword arguments .
'''


def make_shirt(size, text):
    print(f"The shirt is in size {size}. \nIt says:'{text}' on it. ")


make_shirt("XL", "Tét Chagè!")
make_shirt(size="S", text="What a wonderful day!")


