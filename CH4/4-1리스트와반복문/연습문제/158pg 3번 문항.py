numbers=[273,103,5,32,65,9,72,800,99]
for i in numbers : #for 반복문은 리스트에 있는 요소 하나하나가 i라는 변수에 들어가며 반복적으로 출력됨
    if i % 2 == 0:
        print("{}는 짝수입니다.".format(i))
    else:
        print("{}는 홀수입니다.".format(i))

for i in numbers:
    print("{}는 {}자릿수입니다.".format(i,len(str(i))))