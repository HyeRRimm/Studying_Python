# while 반복문 형식/불이 참인경우에만 실행, 거짓이면 while문을 빠져나오면서 print(문장)실행
while 불표현식:
    문장
print(문장)
# while 반복문: for 반복문처럼 사용하기
##EX
for i in range(10): #i=0~9
    print("{}번째 반복입니다.".format(i))

i=1
while i < 10:
    print("{}번째 반복입니다.".format(i))

# while vs for:while쓰는 경우(무한반복문, 반복에 조건이 필요한 경우)

# while 반복문: 상태를 기반으로 반복하기
##EX) 리스트의 요소들 중 해당되는 모든 값 제거하는 경우
###1
list=[7,7,22,24,8,1]
list.remove(7)
print(list) #[7, 22, 24, 8, 1]: 리스트에서 해당 값을 가진 첫번째 요소만 제거

###2
####내 답 : 오류 why?ㅠ
list=[7,7,22,24,8,1]
x=0
value=7
while x < len(list): #0~5
    list.remove(value)
    x += 1
print(list)

####모범 답안
list=[7,7,22,24,8,1]
value=7
while value in list:
    list.remove(value)
print(list)

# while 반복문: 시간을 기반으로 반복하기(파이썬 모듈):CH7
import datetime
present=datetime.datetime.now()
print(present.year) #메소드가 아니니까 present.year() 형태 작성 아님
print(present.month)
print(present.day)

# while 반복문: break/continue
## break: 반복문을 돌면서 계속 실행하다가 조건에 맞으면 반복을 중단함.(반조건=실행문1 실행)
반복문:
실행문 1
if 조건:
break

## continue: 조건에 맞으면 계속 반복문을 돌다가 조건에 안맞아야지 반복문을 탈출하면서 실행가능(반조건=실행문1 실행)
반복문:
if 조건:
continue
실행문1

## EX)사용자가 종료하겠다고 하면 종료하되 종료 안하면 반복문의 횟수 증가시킴(아래 두코드 실행이 다른 코드임)
###1
i = 0
while i < 10:
    my_decision = input("여기서 끝내고 싶니")
    print("{}번의 기회가 남았어".format(i))
    list = ["네", "Y", "y"]
    i += 1
    if my_decision in list:
        break
###2
i=0
my_decision = input("여기서 끝내고 싶니")
list = ["네", "Y", "y"]
while i < 10:
    print("{}번의 기회가 남았어".format(i))
    i += 1
    if my_decision in list:
        break
## EX)1~10범위의 숫자 중에서 5이상의 수만 출력(1~4는 출력되면 안됨=반복문에 갇혀있기, 5이상의 수는 반복문에서 나와서 출력(:실행문1))
i=1
while i < 11: # Q) 11이 왜 출려되는거임?
    i += 1
    if i < 5:
        continue
    print(i)


for i in range(1,11):
    if i < 5:
        continue
    print(i)

