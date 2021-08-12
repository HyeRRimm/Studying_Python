key_list=["name","hp","mp","level"]
value_list=["기사",200,30,5]
character={}
#character사전의 키= key_list의 요소, character사전의 값=value_list의 요소, 두 리스트의 요소들의 인덱스 값이 같음!
#for문을 사용해서 사전에 키: 값 추가.
#구분!

for element in range(len(key_list)):
    character[key_list[element]] = value_list[element]
print(character)

for element in range(0,4):
    character[key_list[element]] = value_list[element]
print(character)

element=0
for element in range(0,4):
    character[key_list[element]] = value_list[element]
    element += 1
print(character)