'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python .
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message .
'''


def make_shirt(size="Large", text ="I love Python"):
    print(f"The shirt is in size {size}. \nIt says:'{text}' on it. ")


make_shirt("M")
make_shirt(size="L")
make_shirt("xs", "CodingNomads")