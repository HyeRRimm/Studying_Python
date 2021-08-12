#리스트 안에 딕셔너리가 있는 경우
#for문을 사용해서 리스트 안의 요소들을 반복적으로 추출
#리스트 안의 요소들은 각각 딕셔너리 형태

pets = [
    {"name":"구름","age":5},
    {"name":"초코","age":3},
    {"name":"아지","age":1},
    {"name":"호랑이","age":1}

]

for line in pets:
    print("{} {}살".format(line["name"], line["age"]))