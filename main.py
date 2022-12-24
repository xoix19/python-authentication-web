import requests

data = requests.get("PASTEBIN").text
# example user:pass

username = input("Username : ")
password = input("Password : ")

if f"{username}:{password}" not in data:
    print("Not Valid ")
else:
    print("Valid")
