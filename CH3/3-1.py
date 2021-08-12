# (1)불 만들기: 비교 연산자 6개 : 숫자, 문자열 모두 적용 가능(문자열 사전순)
==/!=/<,>/<=,>=
print(6 <= 3) #F
print("가방"<"하마") #T

# 불 만들때 비교 연산자, 불끼리 비교할 때 논리 연산자
# 문자열, 숫자열의 대소 비교시 비교연산자

# (2)불 연산하기: 논리 연산자 3개
not/or/and

# 1)not : 단항연산자, 불 자료형 반대로
age= 24
print("{},{}".format("HYERIM", 24<30)
print("{},{}".format("HYERIM", not 24<30)

# 2)or
# 3)and

# (3)논리 연산자의 활용
#1)and
#2)or

# (4)if 조건문: 4칸 들여쓰기

# (5)날짜/시간 활용하기
import datetime #모듈을 사용해서 datetime 정보 가져오기
now= datetime.datetime.now() #함수로 현재 시간을 구해서 변수에 저장
print(now.year, now.month , now.day)

# (6)컴퓨터의 조건: 컴퓨터가 빨리 실행할 수 있는 조건문을 만드는게 포인트!
#예: 짝수, 홀수 구분
#1
number= input("숫자를 입력해주세요") #문자열
if number[-1] in "0,2,4,6,8":
    print("짝수")
else:
    print("홀수")
#2
number= input("숫자를 입력해주세요")
if int(number) % 2 == 0:
    print("짝수")
if int(number) % 2 == 1:
    print("홀수")


