### 모듈 임포트
# requests
import requests

resp = requests.get('http://naver.com')
# print(resp.text)

#### import
# import를 사용하여 해당 모듈 전체를 import
import math

print(math.pi)
print(math.cos(100))

#### from import
# 해당 모듈에서 특정한 타입만 import
from math import pi
from math import cos
print(pi)
print(cos(100))

#### * 임포트
# 해당 모듈내에 정의된 모든 것을 import
# 일반적으로 사용이 권장되지 않음
from math import *
print(sin(100))
print(e)

#### as
# 모듈 import 시, alias(별명) 지정가능
import math as m
print(m.exp(3))
print(m.cos(100))
