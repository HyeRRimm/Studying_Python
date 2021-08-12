#재귀함수: 정의된 함수 안에 같은 함수가 사용되는 함수
#ex)펙토리얼을 나타내는 2가지 방법
#1.
def factorial(n):
    if n==0:
        return 1
    else:
        output=1
        for i in range(1, n+1):
            output *= i
        return(output)
print(factorial(3))

#2.재귀함수 사용해서 함수를 정의하는 경우
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

#재귀함수의 문제점은 상황에 n번째 함수의 값이 그 전 함수의 값들과 연계가 되므로 코드의 반복 횟수가 기하급수적으로 증가함
#결국, 실행속도 점점 느려짐
#이를 위해 메모화 등장!!
#메모화: 한번 계산한 값은 다시 계산하지 않도록 메모장에 입력해서 넣는 시스템
#메모화 예시
dictionary={1:1, 2:1}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output=fibonacci(n-2)+fibonacci(n-1)
        #fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)이지만 f(n)을 정의하는 함수 내부에서 f(n)이 사용되는 것은 모순이므로
        #output을 사용한다.
        dictionary[n]=output
        return dictionary[n]
print(fibonacci(4))

#조기리턴: 함수를 정의하는 코딩 중간에 return문을 써서 (조기에 리턴해서) 이후 함수의 실행을 차단하는 기술
