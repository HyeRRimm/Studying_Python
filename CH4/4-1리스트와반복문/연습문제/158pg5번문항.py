numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]
for number in numbers:
    output[number % 3].append(number) #예를들면 1은 나머지가 1이니까 output리스트의 1번 리스트로 들어감
print(output)
#숫자들을 나눌때 나머지 값을 이용해서 나눌 수 있음을 미리 알아두면 코드 쉽게 짜짐!
#만약 1을 0번인덱스로 넣고 싶으면 output[(number-1) % 3].append(number)로 작성하면 됨.

