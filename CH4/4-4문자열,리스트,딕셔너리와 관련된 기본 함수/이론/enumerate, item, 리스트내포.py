# 리스트에 적용할 수 있는 기본 함수: max(), min(), sum()
max(), min() #리스트, 숫자열 all 가능
sum() #리스트만

# 리스트 뒤집기: reversed(리스트)- 일회용함수
## 리스트 역으로 돌리기
list(reversed(리스트))

## 반복문에 사용하기
for i in reversed(리스트):
    print(i)

# 리스트 속 (인덱스, 요소) 튜플로 확인하기: enumerate()
my_list = [1, 2, 5, 6]
for x, y in enumerate(list):
    print("{}번째 요소는 {}입니다".format(x, y))

print(enumerate(my_list))  # enumerate함수는 list를 객체로서 저장하므로 출력X
print(list(enumerate(my_list)))  # 객체로 저장된 list를 강제로 리스트형으로 자료형변환시켜서 출력O

# 딕셔너리 속 (키, 값) 튜플로 확인하기: items()- 일회용함수
dictionary={
    "name":"HYEIRM",
    "age":"24",
    "Favoriete":"Thinking"
}
for key, value in dictionary.items():
    print("{}의 짝은 {}입니다".format(key,value))

# 리스트 내포
## 1(리스트 내포X)
list=[]
for i in range(3,20,2):
    list.append(i)
print(list)
## 2(리스트 내포O)
list=[i for i in range(3,20,2)]
print(list)
## 3 (리스트 내포X, 조건문 포함)
list=[]
for i in range(3,50,2):
    if i % 3 == 0:
        list.append(i)
print(list)
## 4(리스트 내포O, 조건문 포함)
list=[i for i in range(3,50,2) if i % 3 == 0 ]
print(list)

