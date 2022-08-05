#### variable scope (변수의 범위)
num1 = 10
num2 = 30


def test(num1, num2):
    print(num1, num2)
    return num1 + num2


test(30, 40)
print(num1, num2)


#### variable length argument (가변길이 인자)

# 파라미터를 정의할때 앞에 * 붙이게 되면 그 함수는 호출하는 입장에선 가변길이 함수가 되고 내부적으론 튜플로 인식이 된다.
def test(*x):
    print(type(x))


test(10, 20)


def test_2(*args):  # arguments
    for item in args:
        print(item)


test_2(10, 30, 40)


#### keyword parameter (키워드 파라미터)
def test2(**kwargs):  # key word arguments
    for key, value in kwargs.items():
        print('key:', key, ', value:', value)


test2(a=1, b=2, c=3, d=4, name='Bob', age=90)

# 가변길이 함수의 대표적인 예 **문자열 포맷 함수**

a = '오늘 온도: {today_temp}도, 강수확률은: {today_prob}% 내일온도: {tomorrow_temp}도'.format(tomorrow_temp = 23, today_prob = 40, today_temp = 40)
print(a)
