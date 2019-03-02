
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        return f"User's full name is {self.last_name.upper()} {self.first_name.capitalize()}"

    def greet_user(self):
        print(f"{self.first_name.capitalize()}, welcome!")


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