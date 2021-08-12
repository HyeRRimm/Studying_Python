# 작성 순서
try: #예외가 발생할 가능성이 있는 코드
except: #예외가 발생할 경우 실행할 코드
(finally): #(예외 여부에 관계 없이)무조건적으로 실행하는 코드/ finally코드는 선택

# 작성 예시
try:
    number = int(input("정수를 입력해주세요"))
    print("당신이 좋아하는 수군요")
except:
    print("정수입력하라고요 ㅂㅅ아")
finally:
    print("뭘 썼든 수고하셨습니다다)

#finally 구문 사용 이유: 함수 내부에서 return, 반복문 내부에서 break 사용시 유용함
# 1) 함수 내부에서 return 사용
def example():
    try:
        number = int(input("정수를 입력해주세요"))
        print("당신이 좋아하는 수군요")
        return
    except:
        print("정수입력하라고요 ㅂㅅ아")
    finally:
        print("뭘 썼든 수고하셨습니다")

example()

# 2) 반복문 내부에서 break 사용
# 반복문안에서 break 만나면 반복문을 빠져나가는데 finally 구문은 무조건적으로 실행
while True:
    try:
        number = int(input("정수를 입력해주세요"))
        print("당신이 좋아하는 수군요")
        break
    except:
        print("정수입력하라고요 ㅂㅅ아")
        break
    finally:
        print("뭘 썼든 수고하셨습니다")
