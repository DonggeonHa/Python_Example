#### Lambda 함수

# 이 함수를 한 줄로 쓰는게 Lambda 함수이다. 중요한건 return을 쓰면 안된다.
def square2(x):
    return x ** 2


square = lambda x: x ** 2
print(square(5))  # 25


# 파라미터가 2개 일 때
def add(x, y):
    return x + y


add2 = lambda x, y: x + y
print(add2(10, 20))  # 30


# 문자열 길이에 따라 정렬하고 싶을 때
def str_len(s):
    return len(s)


strings = ['bob', 'charles', 'alexander3', 'teddy']
# 기본적인 sort는 알파벳순서로 정렬을 하는데 key 파라미터를 이용하면 원하는 형태로 정렬이 가능하다.
# strings.sort(key=str_len)
# 함수를 생성해서 파라미터로 넣어도 되지만 람다함수를 이용하면 바로 간단하게 넣을 수 있다.
strings.sort(key=lambda s: len(s))

print(strings)


#### filter, map, reduce
# filter(함수, 리스트)
def even(n):
    return n % 2 == 0


nums = [1, 2, 3, 6, 8, 9, 10, 11, 13, 15]

# print(list(filter(even, nums)))  # [2, 6, 8, 10] ## 람다 함수를 안썼을 때
print(list(filter(lambda n: n % 2 == 0, nums)))  # [2, 6, 8, 10]

# map(함수, 리스트)
# 주어진 리스트, 리스트의 제곱을 한 숫자로 새로운 리스트
nums = [1, 2, 3, 6, 8, 9, 10, 11, 13, 15]
print(list(map(lambda n: n ** 2, nums)))  # [1, 4, 9, 36, 64, 81, 100, 121, 169, 225]

# reduce

import functools

# functools.reduce(함수, 리스트)
a = [1, 3, 5, 8]

print(functools.reduce(lambda x, y: x + y, a))  # 리스트 내의 모든 수의 합 # 17
print(functools.reduce(lambda x, y: x * y, a))  # 리스트 내의 모든 수의 곱 # 120