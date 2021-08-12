my_dictionary={
    "사과":"apple",
    "포도":"grape",
    "망고":"mango",
    "오이":"cucumber"
    }
print(my_dictionary[my_key])
my_key=input("키를 입력해주세요")
value = my_dictionary.get(my_key)
print(value)

if value in my_dictionary[my_key]:
    print(my_dictionary[my_key])
elif value == None :
# if value == "None":
    print("존재하지 않는 키에 접근하려고 하십니다")




