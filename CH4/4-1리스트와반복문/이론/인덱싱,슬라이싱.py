#리스트: 하나의 변수에 여러가지 값을 저장
numbers=["A","B","C","D","E"]
print(numbers[0])
print(numbers[-5])
print(numbers[-6]) # 2바퀴 가능 아이템 3개면  0=-3, 1= -2, 2= -1 -3~2까지 값을 가질 수 있음

#리스트 안의 요소인지 확인
list_1=["H","Y","E","R","I","M"]
print("Y" in list_1)

#인덱싱(리스트의 일부 자료 찾아내기)
print(numbers[1:]) # 1번째 값부터 끝까지 찾아냄
print(numbers[:2]) # 1번째 값까지 찾아냄, 리스트 범위가 끝에 있는 경우 조심!!

#리스트 슬라이싱
new_numbers=numbers[:4] # 잘라낸 리스트로 새로운 리스트 생성
print(new_numbers[1])