#### 함수 연습문제
# 1. 주어진 숫자 리스트의 평균을 구하는 함수를 출력하시오
# 입력: 숫자 리스트
# 출력: 숫자 리스트의 평균값

def mean(nums):
    _sum = 0
    for i in nums:
        _sum += i
    return _sum / len(nums)


def mean2(nums):
    # sum 내장 함수로 대체 가능
    # _sum = 0
    # for i in nums:
    #    _sum += i
    return sum(nums) / len(nums)


print(mean([1, 2, 3]))  # 2.0
print(mean2([1, 2, 3, 4, 5]))  # 3.0
print(mean([1, 2, 3.0, 3.9, 8.7]))  # 3.72


# 2. 해당 숫자가 소수인지 아닌지 판별하시오.
# 소수 판별 (1과 자기 자신으로만 나눠지는 수)
# 입력: 양의 정수 1개
# 출력: boolean (소수: True, 합성수: False)

# 관례 : 함수에서 True, False를 반환시킬땐 변수명 앞에 is_를 붙힌다.
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime(89))  # True 소수
print(is_prime(100))  # False 합성수


# 3. 2부터 해당 숫자사이에 소수가 몇개인지 출력하는 함수를 구하시오
# 2, 3, 4, 5, 6, 7 -> 4
# 2, 3, 4, 5 -> 3
# 입력: 양의 정수 1개
# 출력: 2 ~ 해당 숫자 사이의 소수의 개수

def num_prime(num):
    count = 0
    for i in range(2, num + 1):
        if is_prime(i):
            count += 1
    return count


print(num_prime(7))     # 4
print(num_prime(5))     # 3
print(num_prime(100))   # 25
