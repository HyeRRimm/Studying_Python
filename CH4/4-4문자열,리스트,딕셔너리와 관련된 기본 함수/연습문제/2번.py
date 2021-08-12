#1~100을 이진수로 나타내고->0이 1개인 숫자들의 합 구하기

#step1)1~100자연수 출력
for i in range(1,101):
    print(i)
#step2)1~100을 이진수로 출력
for i in range(1,101):
    binary_digit="{:b}".format(i)
    print(binary_digit)
#step3)이진수 중 0이 1개인 이진수를 출력
for i in range(1,101):
    binary_digit="{:b}".format(i)
    if binary_digit.count("0")==1 :
        print(binary_digit)
#step4)이진수를 십진수로 변경
for i in range(1,101):
    binary_digit="{:b}".format(i)
    if binary_digit.count("0")==1 :
        print("{} :{}".format(int(binary_digit,2),binary_digit))
#step5)십진수의 합
total_sum=0
for i in range(1,101):
    binary_digit="{:b}".format(i)
    if binary_digit.count("0")==1 :
        print("{} :{}".format(int(binary_digit,2),binary_digit))
        total_sum += int(binary_digit,2)
print(total_sum)
#주의: if절 내부에서만 0이 1개인 이진수들이 정의되므로 total_sum도 if 절 내부에서 정의되어야 0이 1개인 이진수를 십진법으로 바꾼 수의 합 출력
#만약 if절을 벗어나면 1~100까지의 합 5050출력

#리스트 내포를 사용해서 표현하기
#십진수,합계 출력
output=[i for i in range(1,101) if "{:b}".format(i).count("0")==1]
print(output)
print("합계:{}".format(sum(output))) #output은 리스트이므로 sum함수를 이용해서 십진수들의 합을 구하면 됌

#십진수:이진수 형태,합계 출력
output=[i for i in range(1,101) if "{:b}".format(i).count("0")==1]
for i in output:
    print("{}:{}".format(i,"{:b}".format(i)))
print("합계:{}".format(sum(output)))