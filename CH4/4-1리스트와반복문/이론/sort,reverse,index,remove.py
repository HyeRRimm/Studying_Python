#in/not in 연산자
list_a=[1,9,7,8,3,4,5,6]
i=0
print(6 in list_a)
#nested list
list_b=[[1,2,3],[4,5,6],[7,8,9]]
print(list_b[0])
print(list_b[0][1])

#sort메소드(sort드메소드 vs sorted함수.py)

#reverse메소드: 리스트의 아이템 값 반대로
## 두 방법의 실행 결과 같음

## 1
list_c=[1,2,9,4,5,16,11]
list_c.reverse()
print(list_c)
## 2
print(reversed(list_c))

#구분! sort메소드의 reverse 파라미터를 사용해서 내림차순으로 정리, reverse 메소드를 이용해 기존 아이템 반대순서로 정리
list_d=[1,5,4,7,9,2]
list_d.sort(reverse=True)
print(list_d)

#index메소드: 리스트의 요소들의 인덱스 값 도출
list_e=[3,6,5,8,9,1,0]
print(list_e.index(1))

#remove메소드(리스트값 편집.py)