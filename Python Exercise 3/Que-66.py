# 66. Create two classes one as a parent and the other as a child. Make a validation whether the child is a subclass of parent or not.

class A:
    x=15
    print("Parent class A")

class B(A):
    print("child class B")
    def add(self,x,y):
        print(x+y)

print(issubclass(B,A))
print(issubclass(A,B))
