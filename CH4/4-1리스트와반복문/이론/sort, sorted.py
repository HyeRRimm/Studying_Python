#함수vs메소드:
# -파이썬이 메소드를 호출하는 것과 파이썬이 함수를 호출하는 것에는 근본적인 차이가 있음.
# - 메소드: 특정 객체에 종속하는 함수로 객체(예:리스트)가 정의되어야 메소드가 정의될 수 있음.

# sorted: 기존 리스트는 건드리지 않고 정렬된 새로운 리스트 리턴
numbers=[2, 25, 34, 59, 52, 11, 19]
new_list = sorted(numbers)
print(new_list) #오름차순
reverse_list = sorted(numbers, reverse=True)
print(reverse_list) #내림차순

#sorted vs sort
numbers=[2, 25, 34, 59, 52, 11, 19]
new_list = sorted(numbers)
print(new_list) # 오름차순
print(numbers) # 원본 유지

numbers=[2, 25, 34, 59, 52, 11, 19]
numbers.sort()
print(numbers) #원본 변화