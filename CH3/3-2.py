#(1)else 조건문의 활용: if 조건문이 거짓일 경우 실행

#(2)elif 구문: 3개 이상의 조건 연결, if 와 else 사이에 삽입되는 조건들

#(3)if 조건문을 효율적으로 사용하기

#(4) False 로 변환: If 조건문을 F로 변환하여 바로 else 구문의 실행문 수행
# *False 로 변환되는 값 4개: None, 0, 0.0 , 빈 컨테이너(리스트, 사전, 튜플, 바이트열, 문자열)
# 예: 메세지 보내기 2가지 방법
message="" #사용자가 입력을 하지 않은 메세지
if message: # F -> "메세지 입력해주세요"
    print("메세지를 전송하였습니다")
else:
    print("메세지를 입력해주세요")

if message != 0 : #T
    print("메세지를 전송하였습니다")
else:
    print("메세지를 입력해주세요")

#(5)pass키워드: IndentationError 안나게하면서 실행하고자하는 기능이 없을 경우 형식상 오류 안나게 하려고
#(6)raise NotImplementedError란 오류 강제 발생
