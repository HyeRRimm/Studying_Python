###내 답
numbers_list = [1,2,3,4,2,3,4,5,7,4,6,8,9,4]
my_answer= {} #{1:1, 2:2, 3:2, 4:4, 5:1, 6:1, 7:1, 8:1, 9:1}

for number in numbers_list:
    print("number:{}".format(number))
    count = my_answer[number]  # 애초에 빈사전이었으므로 key랑 value가 정의가 안된상태임.
    print("count:{}".format(count))
    if count == 0:
        count = 1 #처음 나오는 리스트의 요소이면 딕셔너리에 값이 1인 키 추가
    else:
        count += 1
    my_answer[number] = count
    print("my_ans:{}".format(my_answer))

print(my_answer)


###모범답안
numbers = [1,2,3,4,2,3,4,5,7,4,6,8,9,4]
counter = {} #{1: 1, 2: 2, 3: 2, 4: 4, 5: 1, 7: 1, 6: 1, 8: 1, 9: 1}

for number in numbers: # 요소 in 리스트, 키 in 딕셔너리 , 딕셔너리[키]= value
    if number in counter: #counter 딕셔너리는 빈 사전인데 if 조건문에 해당되는 경우가 읎는데
        counter[number] += 1
        #Q: count= counter[number] 이걸 정의하지 않은상태에서 += 1 코드작성하면 컴터가 count가 value값인지 어떻게 알고 연산함?
    else:
        counter[number] = 1
        #Q
        #딕셔너리에 요소를 추가할 때
        #1st)딕셔너리={}
        #2nd)딕셔너리[key]=value
        #3rd)print(딕셔너리) 이 순서로 진행하는 건데 이 과정을 담고있는 공식이 읎는데?
print(counter)
