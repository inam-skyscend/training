# 15. Call a URL which accepts input and pass it in json format and receive the response in json format.
import requests
from passw import mail_psw

user_dict = {
    "name":"inamhusain2001",
    'pass':mail_psw,
}

#
response = requests.post("https://www.google.com/gmail/",json=user_dict)
print("response", response)
res = response.json()
print(res)

