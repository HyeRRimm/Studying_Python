#(1) 튜플:
# 1) *튜플이 리스트와 다른점 2가지: 대괄호 대신 소괄호 사용가능, 한번 값을 선언하면 값을 바꿀 수 없음.
# 2) 괄호를 생략해도 튜플로 인식할 수 있는 경우라면 괄호를 생략해도 됨.(ex: enumerate함수)
# 3) 여러개의 값을 리턴하고 할당할 수 있으므로 반복문, 리턴문에 많이 사용됨
# 4) 스왑(튜플의 변수 값 바꿔치기)
a,b=10,20
a,b=b,a
print(a,b)

# 5)divmod함수는 튜플 형태로 몫과 나머지를 리턴한다. 괄호 없는 튜플을 리턴하므로 쉽게 변수에 할당하여 지정할 수 있음.
a,b=100,24
print(divmod(a,b))
x,y=divmod(a,b)
print(x)
print(y)
print(type(divmod(a,b)))

# 6) enumerate 함수는 괄호를 생략해도 튜플로 인식할 수 있다.
for i, value in enumerate([1,2,3,4,5]):
    print("{}번째 요소는 {}입니다.".format(i,value))

# 7) 요소가 한개인 튜플 확인
print(type([24,7])) #리스트
print(type((24,7))) #튜플
print(type((24,))) #요소가 1개인 튜플(반드시 , 붙여줘야함 아니면 정수로 출력)
print(type(24)) #정수

# (2) lamda: 함수 2개이상이 얽혀있을 때 사용(내생각)
# 1) 콜백함수
#  콜백함수= 함수 자체에서 또다른 함수를 변수로 사용할 때 직접 정의하는 것이 아니라 외부에서 정의된 함수를 가져와서 사용하는 것
def call_10_times(func):
    for i in range(0,10):
        func()

def print_hello():
    print("안녕하세요")

print(call_10_times(print_hello))

# 아래의 경우 call_10_times 함수의 변수는 func함수이고, func함수의 변수는 i이다 즉 func(i)는 print_hello(number)로 대치된다.
def call_10_times(func):
    for i in range(0,10):
        func(i)

def print_hello(number):
    print("안녕하세요",number)

print(call_10_times(print_hello))

# 2) 등장배경: 콜백함수처럼 매개변수로 함수를 전달하기 위해서 함수 구문을 외부에서 작성하는 것도 번거롭고 코드 공간 낭비라고 생각한 개발자들이 람다라는 개념을 생각함.

# 3) 형식:
def 함수이름(매개변수):             =      lambda 매개변수: 결과
    return 결과
# 예시(람다 사용 x)
def call_10_times(func):
    for i in range(0,10):
        func(i)

def print_hell0(number):
    print("안녕하세요", number)

call_10_times(print_hell0)

#(람다 사용O)
def call_10_times(func):
    for i in range(0,10):
        func(i)

call_10_times(lambda number : print("안녕하세요", number))

# (3) filter() 함수
# 1) 형식: filter(함수, 리터리블):
# 2) 의미: 리터러블 안의 요소들을 함수 안에 넣어서 리턴된 값이 TRUE인 요소들로 이루어진 새로운 리스트를 리턴해준다.
#         다만 filter 함수에 매개변수를 사용할 경우 return 값이 반드시 불이어야한다.
# 예시상황= 1~99 자연수가 있는 리스트에서 짝수만 있는 리스트를 생성하고 싶을 때
# 1) filter함수 사용
def 짝수만(number):
    return number % 2 == 0

a = list(range(100))
b = filter(짝수만, a)
print(b)

# 2) filter, lambda 함수 사용
a = list(range(100))
b = filter(lambda number: number % 2 == 0)
print(list(b))

# 예시상황1)의 경우 콘솔에 값 출력X, 객체만 출력: reverse랑 비슷
# 해결방법1) for i in b :
a = list(range(100))
b= filter(짝수만, a)

for i in b:
    print(i)

# 해결방법2) list로 만든다음 출력
a = list(range(100))
b= filter(짝수만, a)
print(list(b))

# (3)map() 함수
# 1) 의미: 리터러블 안의 요소들을 함수에 넣어서 나온 결과값들로 새로운 리스트를 형성한다
# 2) 형식: map(함수, 리터버블)
#예시: 두 결과 값이 다르다!
list_a=list(range(1,101))
def 짝수만(number):
     return number % 2 == 0
print(짝수만(10))
print(list(map(lambda number : number % 2 == 0, list_a))) #리스트A에 있는 요소들을 람다함수에 넣은 값들을 모두 모아놓음.
print(list(filter(lambda number : number % 2 == 0, list_a))) #리스트A에 있는 요소들 중 리턴값이 참인 요소들만 필터링해서 모아놓음
print([i for i in list_a if i %2==0]) #리스트 내포로도 표현할 수 있음, map, filter 함수는 제너레이터 함수라서 내부의 데이터가 실제로 용량을 차지하지 않는다. 리스트함수로 덮어줘서 출력하면 메모리 용량 차지함.



