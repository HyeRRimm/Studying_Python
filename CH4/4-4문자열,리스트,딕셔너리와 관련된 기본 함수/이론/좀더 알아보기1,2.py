# 좀 더 알아보기1 : 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점
# 조건문과 반복문에 들여쓰기를 한게 출력에도 그대로 나타남
## 문제점: 조건문, 반복문의 4칸 들여쓰기가 그대로 출력
## Q) \랑 \n이랑 같은 건가?
my_number = int(input("숫자를 입력해주세요"))
if my_number % 2 == 0:
    print("""\n
    당신이 입력한 숫자는 짝수입니다.
    {} 짝수라고요. 아시겠어요?""".format(my_number))

    print("""\
     당신이 입력한 숫자는 짝수입니다.
     {} 짝수라고요. 아시겠어요?""".format(my_number))

## 해결책: 마지막을 제외한 문자열의 끝에 이스케이프문자 쓰기

    print(
     "당신이 입력한 숫자는 짝수입니다.\n"
     "{} 짝수라고요. 아시겠어요?\n"
     "좋은 말로 할 때 알아들으시라구요"
         .format(my_number))
## 해결책: join함수와의 콜라보ㅋ
### 구분.join(문자열로 구성된 리스트])
print("::".join(["1","2","3","4"]))

    print("\n".join([
        "당신이 입력한 숫자는 짝수입니다.",
        "{} 짝수라고요. 아시겠어요?",
        "좋은 말로 할 때 알아들으시라구요"]
    ))

# 좀 더 알아보기 2 :이터레이터
#reversed 한수: 리스트 리턴X, 이터레이터 리턴0
#(메모리의 효율성을 위해 기존 리스트를 복사하여 뒤집는 것 보다 기존 리스트를 활용해서 작업하는 것이 효율적)
my_list=[1,2,3,4,5,6]
print(reversed(my_list))
print(list(reversed(my_list)))

#next(): 이터레이터를 이루는 요소들을 순차적으로 출력
new_iterator=reversed(my_list)
print(next(new_iterator)) #6
print(next(new_iterator)) #5