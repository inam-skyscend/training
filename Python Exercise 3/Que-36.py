# 36. Create a regular expression to check a valid email.

import re

com=re.compile("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")

res1=com.match("inamhusain2001@gmail.com")
print(res1)

res2=com.match("inamhusain.momin@skyscendbs.com")
print(res2)

