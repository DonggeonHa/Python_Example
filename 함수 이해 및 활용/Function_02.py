#### Default parameter 사용 시 주의점
def test(a, b, c = 1):
    print(a, b, c)  # 10 20 1

test(10, 20, 1)

#### keyword parameter (키워드 파라미터)
def test(x, y, z):
    a = x + y + z
    return a

test(x=10, y=50, z=3)   # 63

#### return (리턴)
def weird_multiply(x, y):
    if x > 10:
        return x * y

    print(x + y)
    return (x + 2) * y

print(weird_multiply(12, 5))

# 비교
def weird_multiply2(x, y):
    if x > 10:
        return x * y

print(weird_multiply2(2, 5))

#### multiple return (복수 값 반환)
def add_mul(x, y):
    s = x + y
    m = x * y

    return s, m

c = add_mul(20, 3)
print(type(c))
print(c)

a, b = add_mul(20, 3)
print(a, b)