### Class Inheritance(상속)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다'.format(self.name, food))

    def sleep(self, minute):
        print('{}은 {}분동안 잡니다'.format(self.name, minute))

    def work(self, minute):
        print('{}은 {}분동안 일합니다'.format(self.name, minute))


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Employee(부모클래스)
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Student('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)

# Bob은 BBQ를 먹습니다
# Bob은 30분동안 잡니다
# Bob은 60분동안 일합니다

### method override

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다'.format(self.name, food))

    def sleep(self, minute):
        print('{}은 {}분동안 잡니다'.format(self.name, minute))

    def work(self, minute):
        print('{}은 {}분동안 일합니다'.format(self.name, minute))


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self, minute):
        print('{}은 {}분동안 공부합니다'.format(self.name, minute))

# Employee(부모클래스)
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self, minute):
        print('{}은 {}분동안 업무를 합니다'.format(self.name, minute))


bob = Student('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)

bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)

# Bob은 BBQ를 먹습니다
# Bob은 30분동안 잡니다
# Bob은 60분동안 공부합니다

# Bob은 BBQ를 먹습니다
# Bob은 30분동안 잡니다
# Bob은 60분동안 업무를 합니다


### super

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다'.format(self.name, food))

    def sleep(self, minute):
        print('{}은 {}분동안 잡니다'.format(self.name, minute))

    def work(self, minute):
        print('{}은 {}분동안 준비를 합니다.'.format(self.name, minute))


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self, minute):
        super().work(minute)
        print('{}은 {}분동안 공부합니다'.format(self.name, minute))

# Employee(부모클래스)
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self, minute):
        super().work(minute)
        print('{}은 {}분동안 업무를 합니다'.format(self.name, minute))

bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)

# Bob은 BBQ를 먹습니다
# Bob은 30분동안 잡니다
# Bob은 60분동안 준비를 합니다.
# Bob은 60분동안 업무를 합니다