'''
6-6. Polling: Use the code in favorite_languages.py (page 104) .
• Make a list of people who should take the favorite languages poll . Include
some names that are already in the dictionary and some that are not .
• Loop through the list of people who should take the poll . If they have already taken the poll,
print a message thanking them for responding .
If they have not yet taken the poll, print a message inviting them to take the poll .
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'fredrik': 'ruby',
    'arun': 'c#',
    'roi': 'java'
}

names = ['jen', 'sarah', 'edward', 'phil', 'fredrik', 'arun', 'roi', 'ben', 'casey','daniel']


for i in names:
    if i in favorite_languages:
        print(f"{i.capitalize()}, Thank you for responding ot the pool!")
    else:
        print("Please participate in the pool, please!")
