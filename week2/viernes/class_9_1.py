'''
9-1. Restaurant: Make a class called Restaurant .
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indi- cating that the restaurant is open .
Make an instance called restaurant from your class .
Print the two attri- butes individually, and then call both methods .
'''

class Restaurant:
    def __init__(self, name, type, number_served = 0):
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_restaurant(self):
        return f"{self.name.capitalize()} is a {self.type} restaurant."

    def open_restaurant(self):
        return print(f"{self.name.capitalize()} is open now!")

    def __str__(self):
        return f"There are {self.number_served} customer served so far today."

    # 9-4
    # adding an attribute: number_served = 0

    def set_number_served(self, num_of_customer):
        self.num_of_customer = num_of_customer
        self.number_served = self.num_of_customer
        return f"Set the number of customer to {self.number_served}."

    def increment_number_served(self, served_per_day ):
        self.served_per_day = served_per_day
        self.number_served += served_per_day
        return f"Today, we have {self.number_served} customers today."


if __name__ == '__main__':

    sharez = Restaurant("sharez", "Persian")
    print(sharez.describe_restaurant())
    sharez.open_restaurant()