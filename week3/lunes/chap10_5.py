'''
10-5. Programming Poll: Write a while loop that asks people why they like programming .
Each time someone enters a reason, add their reason to a file that stores all the responses .
'''
ans = ""
with open("responses.txt", "a") as f:
    while True and ans != "q":
        ans = input("Why do you like programming? ")
        f.write(ans + "\n")
