# 14. Call any URL and receive the response for it. Print the response text and url.

import requests

response = requests.get("http://spu.ac.in")
print(response, type(response))
print(response.text)
print(response.url)

