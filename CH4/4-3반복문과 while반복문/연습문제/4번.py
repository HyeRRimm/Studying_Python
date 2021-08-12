max_value=0

for i in range(1,100):
    j= 100- i
    current_value= i * j
    if current_value > max_value :
        max_value = current_value
        a= i
        b= i
print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))
# line 8,9의 정의가 없다면 for반복문을 끝낸 i,j,최대값 즉 99, 1, 2500이 최종출력
# line 8,9를통해 최대 곱을 만드는 i,j를 저장해서 최종 a,b 출력해야함.