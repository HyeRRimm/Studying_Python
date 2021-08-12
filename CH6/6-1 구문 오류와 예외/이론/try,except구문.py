# try, except 구문 형식
try:
    #예외가 발생할 수 있는 가능성이 있는 코드
except:
    #예외가 발생했을 때 실행할 코드

#예: 내가 입력한 숫자의 제곱을 출력하고 싶은 경우
while True:
    try:
        print(int(input("숫자를 입력해주세요:"))**2)
        break # 만약 사용자가 숫자 잘 입력하면 제곱 값 출력하고 코드 끝나면서 반복문 종결
    except: #만약 사용자가 입력한 것이 숫자가 아니면 바로 except구문으로 넘어가면서 무한 반복문
        pass # except-pass 짝꿍, 그래야 코드가 죽지 않고 숫자아니면 아무것도 반환하지 않고 무한반복 가능.

#try, except, else 구문 사용 예시, 밑의 두 코드는 같은 코드
#1)
try:
    my_age = int(input("나이를 입력해주세요:"))
except: #try구문에서 예외가 발생할 경우/my_age= input("나이를 입력해주세요:")라고 입력하면 걍 my_age에 문자열 저장하는 거니까 예외발생안함
    print("네나이도모르냐")
else: #예외가 발생하지 않을 경우 실행할 코드
    print("남은 수명은 {}입니다".format(100-my_age))

#2)
try:
    my_age = int(input("나이를 입력해주세요:"))
    print("남은 수명은 {}입니다".format(100 - my_age))
except:
    print("네나이도모르냐")


#3)
my_age = input("나이를 입력해주세요:") #숫자로 이루어진 문자열을 변수 my_age에 저장
if my_age.isdigit(): #문자열을 이루는 요소들이 숫자이면
    print("남은 수명은 {}입니다".format(100 - int(my_age)))
else: #아니면
    print("네나이도모르냐")


