#1번: 리스트 평탄화 기술 범용성 높으니까 잘 알아두기(암기)
before_list=[]
after_list=[]
def flatten(before_list):
    for item in before_list:
        if type(item) == list :
            flatten(item)
        else:
            after_list.append(item)

    return after_list

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(example))

#2번
#1st: 노드,엣지 고려해서 경우를 나누는 방법 종이위에 써보기
#2nd: 종료조건, 반복조건 사용한 코드 작성

#메모화사용X
앉힐수있는최소사람수=2
앉힐수있는최대사람수=10
전체사람수=100
count = 0
#트리: 노드=남은사람수, 엣지=앉힌사람수
def 문제(남은사람수,앉힌사람수):
    global count
    #종료조건 2개
    if 남은사람수<0:
        return 0
    if 남은사람수 == 0:
        count += 1
    #재귀처리
    else: #i=두번째이상 단계의 엣지, 전단계 엣지 이상의 수~10까지 해야 2+4, 4+2의 중복 피할 수 있음
        for i in range(앉힌사람수,11):
            문제(남은사람수-i,i)
    return count

#메모화 사용 O
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람수 = 100
memo = {}


def 문제(남은사람수, 앉힌사람수):
    global count
    # 종료조건 3개
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1
    key = str([남은사람수, 앉힌사람수])
    if key in memo:  # 메모 안에 키가 있으면 더이상 계산하지 않고 값을 그대로 돌려줌(?)
        return memo[key]  # memo={(남은사람수,앉힌사람수):경우의 수} 형태로 저장한다.key값이 memo딗셔너리안에 있으면 count 계산없이 바로 리턴.

    # 재귀처리
    count = 0
    # i=앉힌사람수= 두번째이상 단계의 엣지는 전단계 엣지 이상의 수~10까지 해야 문제의 조건에 맞게 2+4, 4+2의 중복 피할 수 있음
    for i in range(앉힌사람수, 11):
        count += 문제(남은사람수 - i, i)

    # 메모화처리
    memo[key] = count
    return count # 함수인 문제(남사람수,앉힌사람수)가 무엇을 출력하는 함수인지에 대한 설명

print(문제(전체사람수, 앉힐수있는최소사람수))











