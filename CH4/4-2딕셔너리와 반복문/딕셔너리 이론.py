#사전 (키:값 1쌍이룸)
my_dictionary={
    "사과":"apple",
    "포도":"grape",
    "망고":"mango",
    "오이":"cucumber"
    }
#사전 안의 값 존재여부 확인
print("사과" in my_dictionary)
print("배" in my_dictionary)

#사전 안의 모든값 출력
for value in my_dictionary.values():
    print(value)
for key in my_dictionary.keys():
    print(key)

#요소 추가하기
my_dictionary["배"]="pear"
print(my_dictionary)

#요소 제거하기, keyError: 키를 기반으로 값을 저장할 때 없는 키를 검색하거나 제거하려는 경우
del my_dictionary["사과"]
print(my_dictionary)

#get(): 존재하지 않는 키에 접근할 경우 keyError가 아닌 None 출력
my_key=input("키를 입력해주세요")
value = my_dictionary.get(my_key)
if value in my_dictionary[my_key]:
    print(my_dictionary[my_key])
if value == None:
    print("존재하지 않는 키에 접근하려고 하십니다")

#내부에 키의 존재 확인
my_key = input("키를 입력해주세요")
if my_key in my_dictionary:
    print(my_dictionary[my_key])
else:
    print("잘못된 키에 접근하고 있습니다")

#키,value 한쌍 출력하는 2가지 방법: 리스트는 enumerate(), 사전은 items(): 튜플 형태로 출력
리스트=[]
딕셔너리={}

for i,value in enumerate(리스트):
    print(i,value)

for key,value in 딕셔너리.items():
    print(key,value)

#키, 값 리스트 따로따로 만들기
for i in my_dictionary.keys():
    print(i)
for i in my_dictionary.values():
    print(i)

