import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

url = "https://www.instagram.com"
payload = {'inUserName': 'martin.breuss', 'inUserPass': 'Bali2019'}
res = requests.get(url,  data = payload)
print("ok" if res.status_code == 200 else "check your url")
print(res.headers)

with open("instagram.html", 'w', encoding='utf-8') as f:
    f.write(res.text)
