# 35.Create a regular expression to check a valid URL.

import re
com = re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")

res=com.match("https://www.example.com")
print(res)
res=com.match("http://www.example.com/products?id=1&page=2")
print(res)
res=com.match("http://255.255.255.255")
print(res)
res=com.match("http://invalid.com/perl.cgi?key=|http://web-site.com/cgi-bin/perl.cgi?key1=value1&key2")
print(res)

