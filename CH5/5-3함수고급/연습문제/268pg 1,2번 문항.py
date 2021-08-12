## 1번
numbers=[1,2,3,4,5,6]
print("::".join(map(str,numbers)))

#str,map: 모두 파이썬 내장함수
#str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수
#map(함수, 리터러블)는 리터러블안의 요소들을 함수에 넣어서 나온 객체를 돌려주는 함수이다(객체 O, 값X)
#예
literable=(3,4,5,6)
print(list(map(str,literable)))

## 2번
numbers=list(range(1,101))

print("#홀수만 출력하기")
def 홀수만(i):
    return i % 2 == 1
print(list(filter(홀수만,numbers)))

print(list(filter(lambda i: i % 2 ==1, numbers)))
# ---------
print("#3이상, 7미만 추출하기")
def 부분만(i):
    return 3 <= i <7
print(list(filter(부분만,numbers)))

print(list(filter(lambda i : 3 <= i <7, numbers)))
# -----------
print("#제곱해서 50미만 추출하기")
def 제곱(i):
    return i * i < 50
print(list(filter(제곱,numbers)))

print(list(filter(lambda i: i * i < 50, numbers)))