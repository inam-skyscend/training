# 69. Sort the following list with the second element of the inner list. [[4, ’a’], [9, ’x’],[10, ’c’], [25,’z’], [32, ‘b’]].

l1=[[4,'a'], [9,'x'],[10, 'c'], [25,'z'],[32,'b']]
res = sorted(l1, key=lambda e: e[1])
print(res)
