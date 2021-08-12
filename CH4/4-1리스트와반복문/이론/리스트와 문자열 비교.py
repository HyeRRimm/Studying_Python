#리스트와 문자열의 공통점
#-1 인덱싱
list_1=["A","B","C","D","E"]
print(list_1.index("C"))

sentence="HYERIM"
print(sentence.index("H"))
print(sentence[2])

#-2 for 반복문
list_1=["A","B","C","D","E"]
for x in list_1:
    print(x)

sentence="HYERIM"
for x in sentence:
    print(x)

#-3 슬라이싱
list_1=["A","B","C","D","E"]
print(list_1[0:2])

sentence="HYERIM"
print(sentence[0:2])

#-4 덧셈연산
list_1=["A","B","C","D","E"]
list_2=["F","G","H"]
print(list_1+list_2)

sentence_1="HYERIM"
sentence_2="BETHEBEST"
print(sentence_1+sentence_2)

#-5 len함수: 문자열의 길이, 리스트 요소의 갯수
list_1=["A","B","C","D","E"]
print(len(list_1))

sentence="HYERIM BEST!"
print(len(sentence))

#리스트와 문자열의 차이점
#-1 수정 여부
list_1=["A","B","C","D","E"]
list_1[0]="F"
print(list_1)

sentence="HYERIM BEST!"
sentence[0]="z"
print(sentence) #문자열은 수정 불가능
