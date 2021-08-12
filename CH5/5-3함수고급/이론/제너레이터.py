# 제너레이터, yield 키워드가 정확히 뭔지 몰라도 framework에서 yield 키워드 사용하라고 하면 그 때 사용하면 됌ㅋ
# 제너레이터 함수는 제너레이터 객체를 리턴함. 제너레이터는 콘솔에 출력X
# 값 출력 하려면 next() 사용 : next(함수())
# return문 처럼 yield뒤의 값 까지 출력하려면 print사용: print(next(함수()))

# yield키워드는 함수 내부에 여러개 박을 수 있음
# yield = 양보하다, 내 이후의 코드는 실행 안할테니까 돌아가줘

def 함수():
    print("출력A")
    yield 100
    print("출력B")
    yield 200
    print("출력C")
    yield 300


# (1) 함수() 호출
A = 함수()
next(A)
# 함수의 값들이 변수 A에 지정되어서 첫번째 next(A)는 yield100에서 멈추고
next(A)
# 두번째 next(A)는 yield100 에서 다시 실행되면서 "출력B"를 출력하고 yield200에서 멈추기
next(A)
# 세번째 next(A)는 yield 200에서 다시 실행되면서 "출력C"를 출력하고 yield300에서 멈추기
next(A)
# next함수를 호출한 이후 yield 키워드를 만나지 못하고 함수의 값들이 끝나버리면 stopiteration이라는 예외가 발생함
# 즉 next함수가 종료되는 지점에 yield가 있어야만 값이 출력가능!

# (2) 아래의 경우는 함수의 값들이 변수에 따로 지정되지 않아서 yield변수로 잠시 함수의 진행이 멈췄던 지점들이 휘발성으로 날라간다
# 즉 next(함수())를 진행할 때마다 멈춘 지점이 yield100으로 동일하다.
next(함수())
next(함수())
next(함수())

# (3) for 반복문에서의 활용
def 함수():
    print("출력A")
    yield 100
    print("출력B")
    yield 200
    print("출력C")
    yield 300

# for 반복문은 Stopiteration까지 모두 호출을 마친 상태이므로 두번째 for 반복문에서는 출력되는게 없다.
값=함수()
for i in 값:
    print(i)

for i in 값:
    print(i)

# 제너레이터 함수를 호출하는 순간에 내부의 코드가 실행되는 것이 아니라 반복문에서 활용할 때 내부 코드 실행 시작.
# 예: 지연로드(Lazy Load)활용에 사용 가능.
# 예: 제너레이터 함수를 이용한 reversed 반복문 생성
def 반전(리스트):
    for i in range(len(리스트)):
        yield 리스트[-i -1]

값 = 반전([0,1,2,3,4,5])
#변수 "값" 은 함수의 값이 아니라 객체에 불과(메모리 차지X)

for i in 값:
    print(i)



