#(1)문자열의 format()함수
# 1) Index Error
print("{},{}".format(1,2,3,4)) # 1,2 출력
print("{},{},{}".format(1,2)) #IndexError

#(2)format()함수의 다양한 기능
# 1) 정수 출력의 다양한 형태 : 정수를 특정 칸에 출력하기 / {:d}형식을 사용하면 매개변수로 정수만 올 수 있음
output_b="{:5d}".format(52)
output_c="{:05d}".format(52)

output_d="{:+5d}".format(52) #기호 뒤로 밀기, xx+52
output_e="{:+05d}".format(52) #빈자리 0으로 채우면서 기호를 뒤로 밀수 없음, 그냥 +붙이고 빈자리 0으로 채우기, +0052
output_f="{:=+5d}".format(52) #기호 앞으로 당기기, +xx52
output_g="{:=+05d}".format(52) #기호 앞으로 당기기, 빈자리 0으로 +0052

# 2) 소수형 출력의 다양한 형태 {:f}
output_a="{:f}".format(7.24)
output_b="{:15f}".format(7.24)
output_c="{:+15f}".format(7.24)
output_d="{:=+15f}".format(7.24)
output_e="{:+015f}".format(7.24)

# 3) 의미없는 소수점 제거하기 {:g}
A = 7.240
output_a="{:g}".format(A)

#(3) 대소문자 바꾸기: upper(): 모두 대문자로, lower(): 모두 소문자로, 원본 유지
A = "Do your best, oppotunity will come to me, just catch it"
print(A. upper())
print(A.lower())
print(A)

# (4) 문자열 양 옆의 공백 없애기: strip() (공백: 띄어쓰기, 탭, 줄바꿈),(문자열 사이의 공백은 그대로)
A= "\n\n\n   Do your best opportunity will come to me just catch it\n\n  "
print(A.strip())

# (5) 문자열의 구성 파악하기: is~()
.isalnum() : 문자열이 알파벳 또는 숫자로만
.isalpha() : 문자열이 알파벳으로만
.isdigit() : 문자열이 숫자로 인식 가능
.isspace() : 문자열이 공백으로만
.islower() : 문자열이 소문자로만
.isupper() : 문자열이 대문자로만
.isdecimal() : 문자열이 정수형태
.isidentifier() : 문자열이 식별자로 사용 가능

A="Because I'm 24, I wanna try everything"
print(A.isalnum()) #T/F

# (6) 문자열 찾기: find(), rfind()
A= "점장 성격 졸라 짜증남 점장 성격 개병신 ㅅㅂ 나도 병신"
print(A.find("점장"))
print(A.rfind("점장")) #문자열의 오른쪽으로부터 해당 문자있는지 찾기. 인덱스는 왼쪽으로부터 카운트.

# (7)문자열 in 연산자: ~ in ~
A="Because I'm 24, I wanna try everything"
print("24" in A)

# (8)문자열 자르기: split()
A="Because I'm 24, I wanna try everything"
print(A.split(" ")) #공백을 기준으로 문자열을 잘라서 요소로 정리




