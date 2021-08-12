#2번: 리턴파일에 존재
#3번 문항의 4번
def function(valueA=10, valueB=20,*values):
    print(values)
    print(valueA)
    print(valueB)

print(function(1,2,3,4,5))