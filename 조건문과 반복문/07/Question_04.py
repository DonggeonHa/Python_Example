# 4번 문제 : a = [22, 1, 3, 4, 7, 98, 21, 55, 87, 99, 19, 20, 45] 에서 평균을 구하세요.

# while
i = 0
_sum = 0
while i < len(a):
    _sum += a[i]
    i += 1

print(_sum / len(a))

# for
_sum = 0
for x in a:
    _sum += x

print(_sum / len(a))