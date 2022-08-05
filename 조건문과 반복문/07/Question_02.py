# 2번 문제 : 1 - 100까지 정수 중 2의 배수 또는 11의 배수를 모두 출력하시오
nums = list(range(1, 101))
for x in nums:
    if x % 2 == 0 or x % 11 == 0:
        print(x)