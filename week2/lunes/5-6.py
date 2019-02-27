'''
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life .
Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby .
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler .
• If the person is at least 4 years old but less than 13, print a message that the person is a kid .
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager .
• If the person is at least 20 years old but less than 65, print a message that the person is an adult .
• If the person is age 65 or older, print a message that the person is an elder .
'''

age = 76

if age < 2:
    print("He/She is a baby.")
elif 4 > age >=2 :
    print("He/She is a toddler.")
elif 13 > age >= 4:
    print("He/She is a kid.")
elif 20> age >= 13:
    print("He/She is a teenager.")
elif 65 > age >= 20:
    print("He/She is an adult.")
else:
    print("He/She is an elder.")