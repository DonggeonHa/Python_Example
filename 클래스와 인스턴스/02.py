### __init__

class Person:
    def __init__(self):
        print(self, 'is generated')


p1 = Person()
p2 = Person()

# <__main__.Person object at 0x000001C69924CFD0> is generated
# <__main__.Person object at 0x000001C69924CF10> is generated

class Person:
    def __init__(self, name, age=10):
        # print(self, 'is generated')
        self.name = name
        self.age = age


p1 = Person('Bob', 30)
p2 = Person('Kate', 20)
p3 = Person('Aaron')

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)

# Bob 30
# Kate 20
# Aaron 10

### self

