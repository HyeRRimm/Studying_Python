character = {
    "name" : "기사",
    "level" : "12",
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for new_key in character[key]:
            print("{} : {}".format(new_key, character[key][new_key]))
    if type(character[key]) is str:
        print("{} : {}". format(key, character[key]))
    if type(character[key]) is list:
        for item in character[key]:
            print("{} : {}".format(key, item))
