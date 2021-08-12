#1.리스트에 적용할 수 있는 기본 함수: max(), min(), sum()
#2.리스트 뒤집기: reversed()
#3.리스트를 (요소, 인덱스)튜플 형태로 확인 : enumerate()
#4.딕셔너리를 (key,value)튜플 형태로 확인: items()
#2~4=일회용함수(제너레이터): 반복문 사용시 유의하자

#1.
list_a=[1,2,3,4,5]
print(max(list_a)) #max,min의 변수로 리스트, 숫자열 모두 가능하지만 sum은 오직 리스트만 가능
print(min(list_a))
print(sum(list_a))

#2.
list_b=[0,1,2,3,4,5]
for i in reversed(list_b):
    print(i)
for i in reversed(list_b):
    print(i)

list_c=[1,2,3,4,5,6]
#암기: 반복문에 사용할 경우 for i in reversed(리스트): / 리스트 뒤집을 경우 print(list(reversed(리스트)))
#아래의 두번째 반복문은 출력X, 일회용함수라서 변수에 넣어서 사용하는 형태는 작동하지 않음
reversed_c=reversed(list_c)
for i in reversed_c:
    print(i)
for i in reversed_c:
    print(i)

#3.
#암기: 반복문에 사용할 경우 for i, element in enumerate(리스트):
list_d=["H", "Y", "E", "R", "I", "M"]
enumerate(list_d)
print(enumerate(list_d)) #리스트 출력X
print(list(enumerate(list_d))) #리스트 출력0 (요소와 인덱스가 한 쌍인 튜플이 요소로 이루어진 새로운 리스트 출력)

for i,value in enumerate(list_d): #튜플 출력
    print(i,value)

#4.
#암기: 반복문에 사용할 경우 for key,value in 딕셔너리.items():
my_character={
    "name":"HYERIM",
    "age":"24",
    "idol":"everything"
}
for key,value in my_character.items(): #튜플 출력
    print(key,value)