numbers=[]
polling_active = True

while polling_active:
    number= int(input("Plese enter a number: "))
    numbers.append(number)
    if len(numbers) == 5:
        polling_active = False # break
print(numbers)