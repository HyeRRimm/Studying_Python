#예외 객체: 예외 정보는 예외 객체에 데이터로서 저장됨
# 예시
# 1)
try:
    list = [10,20,30,40,50]
    my_number = int(input("0~4 사이의 정수를 입력해주세요"))
    print(list[my_number])
except Exception as exception:
    print(type(exception))
    if type(exception) is ValueError: # 숫자대신 문자 입력한경우
        print("입력하신 값에 문제가 있습니다")
    if  type(exception) is IndexError: # 0~4 이외의 숫자를 입력한 경우
        print("저희가 제공하는 값은 0~4까지입니다")
    else:
        print("알 수 없는 예외가 발생했습니다")

# 2) except + 들여쓰는 if 구문 은 복잡하니까 개발자들은 if 구문과 유사한 "exception 예외 클라스 as 예외 객체: 실행문" 만듦.
try:
    list = [10,20,30,40,50]
    my_number = int(input("0~4 사이의 정수를 입력해주세요"))
    print(list[my_number])
except ValueError as exception:
    print("입력하신 값에 문제가 있습니다")
except IndexError as exception:
    print("저희가 제공하는 값은 0~4까지입니다")
except Exception as exception: # value error, Index error 둘다 아니고 그 외의 예외의 경우
    print("알 수 없는 예외가 발생했습니다")


#예외 구분 방법
#예외 강제 발생
