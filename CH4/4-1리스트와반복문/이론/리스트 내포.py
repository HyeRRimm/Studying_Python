#리스트 내포:반복문을 사용한 리스트 생성을 간결하게 함
list_a=[]
for i in range(0,21,2):
    list_a.append(i)
print(list_a)
#위를 간결하게 아래와 같이 작성
list_a=[]
list_a=[i for i in range(0,21,2)]
print(list_a)

#조건을 활용한 리스트 내포
list_a=[]
for i in range(0,21,2):
    if i % 3 == 0:
        list_a.append(i)
print(list_a)
#위를 간결하게 아래와 같이 작성
list_a=[i for i in range(0,21,2) if i % 3 == 0]
print(list_a)