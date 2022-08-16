### method 정의

# 1. 숫자를 하나 증가
# 2. 숫자를 0으로 초기화

class Counter:
    def __init__(self):
        self.num = 0

    def increment(self):
        self.num += 1

    def reset(self):
        self.num = 0

    def print_current_value(self):
        print('현재값은: ', self.num)


c1 = Counter()
c1.print_current_value()
c1.increment()
c1.increment()
c1.increment()
c1.print_current_value()

c1.reset()
c1.print_current_value()

# 현재값은:  0
# 현재값은:  3
# 현재값은:  0


### method type
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Math.add(10, 20))
print(Math.multiply(10, 20))

# 30
# 200
