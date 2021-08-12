#return문: 처음으로(함수출력) 되돌아가라!(함수 작동 순서 중요)
def success(매개변수1,매개변수2,매개변수3): #2
    print("plan" + str(매개변수1)) #3
    print("try" + str(매개변수2)) #4
    return 1 #5/ 그냥 가지말고 숫자1들고 돌아가!(츤데레함수ㅎㅎ)
    print("re-think" + str(매개변수3))
print(success(1,2,3)) #1 #6
#7
#결국 re-think는 출력X

def success(매개변수1,매개변수2,매개변수3): #2
    print("plan" + str(매개변수1)) #3
    print("try" + str(매개변수2)) #4
    return
    print("re-think" + str(매개변수3))

print(success(1,2,3))
# 아무것도 리턴하지 않았으므로 콘솔에는 plan1 try2 none 출력

#기본적인 함수의 활용
#ex1)범위 내부의 정수를 모두 더하는 함수
def sum_all(start,end):
    total_sum=0
    for i in range(start, end+1):
        total_sum += i
    return(total_sum)
print(sum_all(1,100))

#ex2)범위 내부의 정수를 모두 곱하는 함수(05-1 2번)
def mul(*values):
    total_mul=1
    for i in values:
        total_mul *= i
    return(total_mul)
print(mul(1,2,3,4,5))
#암기: 초기값(total_sum, total_mul)을 설정할 때 연산을 해도 값에 아무런 변화를 주지 않는 것을 사용한다.