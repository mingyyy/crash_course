'''
10-3. Guest: Write a program that prompts the user for their name .
When they respond, write their name to a file called guest.txt .
'''
# 'a' = append
# 'r' = read
# 'w' = write / overwrite


name = input("Please tell me your name: ")
with open("guest.txt","w") as f:
    f.write(name)
