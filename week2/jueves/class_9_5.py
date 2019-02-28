'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166) .
Write a method called increment login_attempts() that increments the value of login_attempts by 1 .
Write another method called reset_login_attempts() that resets the value of login_ attempts to 0 .
Make an instance of the User class and call increment_login_attempts() several times .
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts() .
Print login_attempts again to make sure it was reset to 0 .
'''


class User:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        return f"User's full name is {self.last_name.upper()} {self.first_name.capitalize()}"

    def greet_user(self):
        print(f"{self.first_name.capitalize()}, welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Michael", "Jordan")
# call increment 5 times
for i in range(5):
    user1.increment_login_attempts()
# print the login_attempts shows 5
print(user1.login_attempts)
# reset the login_attempts to 0
user1.reset_login_attempts()
# print the login_attempts shows 0
print(user1.login_attempts)