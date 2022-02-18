class Parent:
    def name(self):
        print("parent")

    def demo(self):
        print("Hello everyone")


class Child(Parent):
    def sample(self):
        print("Child")


p = Parent()
c = Child()

p.name()
p.demo()
# p.sample()          AttributeError: 'Parent' object has no attribute 'sample'

c.sample()
c.name()
c.demo()


