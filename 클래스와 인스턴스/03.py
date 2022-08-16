### self

class Person:
    def __init__(self, name, age=10):
        print('self: ', self)
        self.name = name
        self.age = age

    def sleep(self):
        print('self: ', self)
        print(self.name, '은 잠을 잡니다.')


a = Person('Bob', 30)
b = Person('Kate', 20)

print(a)
print(b)

a.sleep()
b.sleep()

# self:  <__main__.Person object at 0x0000020AE3C3CEB0>
# self:  <__main__.Person object at 0x0000020AE3C3CDC0>
# <__main__.Person object at 0x0000020AE3C3CEB0>
# <__main__.Person object at 0x0000020AE3C3CDC0>
# self:  <__main__.Person object at 0x0000020AE3C3CEB0>
# Bob 은 잠을 잡니다.
# self:  <__main__.Person object at 0x0000020AE3C3CDC0>
# Kate 은 잠을 잡니다.