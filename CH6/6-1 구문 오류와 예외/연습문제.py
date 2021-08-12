# <1번>
구문오류: 코드의 문법적 오류.
예외: 코드의 문법적 오류는 없지만 코드가 실행하다가 죽어버림.

# <2번>: 사용자가 입력한 값이 리스트 내부에 있는지를 확인
# 1) 조건문을 사용한 코드
numbers=[52, 273, 32, 103, 90, 10, 275]
print("#(1)요소 내부에 있는 값 찾기")
my_number= input("수를 입력해주세요") #문자열
if int(my_number) in numbers :
    print("{}는 {}위치에 있습니다".format(my_number, numbers.index(int(my_number))))
else:
    print("리스트 내부에 없는 값입니다.")

# 2)try, except 을 사용한 코드
numbers=[52, 273, 32, 103, 90, 10, 275]
print("#(1)요소 내부에 있는 값 찾기")

try:
    my_number = input("수를 입력해주세요") #문자열
    print("{}는 {}위치에 있습니다".format(my_number, numbers.index(int(my_number))))
except:
    print("리스트 내부에 없는 값입니다.")

# <3번>
#1)예외: Type Error
#2)예외: Value Error
#3)구문오류: Syntax Error
#4)예외: Index Error
