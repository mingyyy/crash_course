my_list = [1,2,3,5,21]

for i in my_list:
    print(i)

count = 1
while count <= 5:
    print("hello")
    count += 1

name = input("You name please:")

flag = True
while flag: # flag == True
    answ = input("what do you want? ")
    if answ == 'quit':
        flag = False

name = ''
while name != "your name":
    name = input(" Tell me your name:")
    if name == 'quit':
        break # get out of the nearist loop
    if name == "martin":
        continue # skip what's after and continue with the loop


