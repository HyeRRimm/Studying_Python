#리스트 연산자 + , *
list_a=[1,2,3]
list_b=[4,5,6]
print(list_a + list_b)
print(list_a * 3)

#요소 추가(append, insert, extend)/ 비파괴적 처리: 기존 리스트에 변화 없음(+), 파괴적 처리: 기존 리스트에 변화 있음(extend)
# append, insert: 요소 1개만 , extend: 요소 여러개
list_a.append(4)
print(list_a)
list_a.insert(0,4)
print(list_a)
list_a.extend(list_b)
print(list_a)

#요소 제거: 2가지 방법(인덱스로 제거하기(del,pop), 값으로 제거하기(remove,clear))
#암기팁: 델리팝! 델리만쥬에서 팝콘 튀김, 뭐하는 함수인지 기능이 딱 보이는 remove, clear 함수들은 단도직입적이므로 바로 값을 작성!
list_c=[7,8,9,10,11,13]
print("list c는 {}입니다".format(list_c))
del list_c [2] # del 리스트명 [인덱스]
print(list_c)
del list_c [0:2] # 0~1 제거
print (list_c)
del list_c [1:] # 1~끝까지 제거
print(list_c)

list_d=[8,1,7,22,24,7]
print("list d는 {}입니다".format(list_d))
list_d.pop(2) # 리스트명.pop (인덱스)
print(list_d)
list_d.pop() # pop함수의 매개변수에 아무것도 들어가지 않으면 리스트의 마지막 요소 제거
print(list_d)

list_e=[1,3,5,7,9,11]
print("list e는 {}입니다".format(list_e))
list_e.remove(3) # remove.(아이템 값) / 단 기존 리스트에서 첫번째로 x값인 아이템을 제거 만약 리스트에서 3이 2개이상이라면 첫번째 3만 제거되어서 나옴
print(list_e)

list_f= [2,4,6,8,10]
print("list f는 {}입니다".format(list_f))
list_f.clear() # 리스트의 전체 값 날려버림
print(list_f)