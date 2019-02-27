'''
7-10. Dream Vacation: Write a program that polls users about their dream vacation .
Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll .
'''
dream_vacation = ""
while dream_vacation != "new york":
    dream_vacation = input("If you could visit one place in the world, where would that be? ").lower()
    print(dream_vacation)
