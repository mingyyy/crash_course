'''
9-2. Three Restaurants: Start with your class from Exercise 9-1 .
Create three different instances from the class, and call describe_restaurant() for each instance .
'''

from class_9_1 import Restaurant as res

a = res("Mother", "Vegan")
print(a.describe_restaurant())

b = res("sage", "Infusion")
print(b.describe_restaurant())

c = res("ashikaya", "Janpanese")
print(c.describe_restaurant())
c.open_restaurant()