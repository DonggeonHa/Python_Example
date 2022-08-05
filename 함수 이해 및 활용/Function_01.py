### 함수?

# 내장 함수의 예
a = [1, 2, 3, 4]
length = len(a)
print(length)

summation = sum(a)
print(summation)


#### 함수의 정의
def add(x, y):
    n = x + y
    return n

c = add(30, 300)
print(c)

#### 함수의 사용(호출)
d = add(30, 40)
print(d)

#### 함수 네이밍(naming)
# 의미에 맞지않는 함수명은 사용하지 말자
def substract(x, y):
    sub = x - y
    return sub

print(substract(4, 3))

#### parameter(argument)(인자)
def test():
    print('haha')
    print('good')

    return 100

a = test()
print(a)

#### Default parameter(기본 인자)
def add2(x, y, z=5):
    a = x + y + z
    return a

add2(10, 20)

# 기본 파라미터의 다른 예
print(1, 2, 3, sep='!', end='%%%')  # 1!2!3%%%
print(2, 3, 4, sep='p') # 2p3p4