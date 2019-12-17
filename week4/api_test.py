# import requests
#
# params ={
#     'type': 'trivia',
#     'notfound': 'floor'
# }
# userinput=int(input("Enter a number:"))
# url = f"http://numbersapi.com/{userinput}?type={params['type']}&notfound={params['notfound']}&fragment"
#
# r = requests.get(url)
# # print(type(r))
# # print(r.text)
#
# # some program
# print(f"we now have more users than {r.text}")

import requests

url = "https://api.datamuse.com/words?rel_rhy=forgetful"
result = requests.get(url)
formatted = result.json()
print(type(formatted))
for i in formatted:
    print(i)
