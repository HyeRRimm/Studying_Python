# 범위
range(0,5) #0,1,2,3,4
range(0,5,2) #0,2,4
# for 반복문: 범위와 함께 사용하기
for i in range(0,5):
    print(i)

# for 반복문: 리스트와 범위 조합하기:
# 암기!!: range(len(리스트)): 리스트 속 요소들이 몇번째 출력인지 알아내기
list=[7,22,24,8,1]
for i in range(len(list)): # i=0~4
    print("{}는 {}번째 요소입니다".format(list[i],i))

# for 반복문: 반대로 반복하기:reversed함수
list=[7,22,24,8,1]
for i in reversed(range(len(list))): # i=4~0
    print("{}는 {}번째 요소입니다".format(list[i],i))
