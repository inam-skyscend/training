# 39. Optimize the following code and make it in two lines.

x = {'a':1, 'b':2}
# if 'c' in x:
#     y = x['c']
# else:
#     y = 0

print((x['c'] if 'c' in x else 0))