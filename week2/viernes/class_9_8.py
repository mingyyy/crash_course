'''
9-8. Privileges: Write a separate Privileges class .
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7 .
Move the show_privileges() method to this class .
Make a Privileges instance as an attribute in the Admin class .
Create a new instance of Admin and use your method to show its privileges .
'''

from class_9_3 import User
from class_9_7 import Admin

class Privileges():
    privileges = ["can add post", "can delete post", "can ban user", "can block user", "can delete user",
                  "can add user"]

    def show_privileges(self):
        l = ""
        for i in self.privileges:
            l += ("- " + i + "\n")
        return f"There are {len(self.privileges)} attributes for Admins: \n" + l

class Admin(User):
    p = Privileges()

    def display(self):
        return f"{self.first_name.title()} has some privileges.\n" + self.p.show_privileges()

print(Admin("martin", "python").display())



