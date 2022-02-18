# 17. Using pickle dump no of variables with different data types in a file 'my_variables.data'.

import pickle

f=open("my_variable.data","wb")

name="inam"
rollno=57
a = [1, 2, 3]
b = {'a': 1, 'b': 2}

pickle.dump(name,f)
pickle.dump(rollno,f)
pickle.dump(a,f)
pickle.dump(b,f)

f.close()