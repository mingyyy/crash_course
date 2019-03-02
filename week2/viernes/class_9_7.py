'''
9-7. Admin: An administrator is a special kind of user .
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on .
Write a method called show_privileges() that lists the administrator’s set of privileges .
Create an instance of Admin, and call your method .
'''

from class_9_3 import User

class Admin(User):
    privileges = ["can add post", "can delete post", "can ban user", "can block user", "can delete user", "can add user"]
    def show_privileges(self):
        l=""
        for i in self.privileges:
            l += ("- " + i +"\n")
        return f"There are {len(self.privileges)} attributes for Admins: \n" + l

caden = Admin("Caden", "Python")
print(caden.show_privileges())