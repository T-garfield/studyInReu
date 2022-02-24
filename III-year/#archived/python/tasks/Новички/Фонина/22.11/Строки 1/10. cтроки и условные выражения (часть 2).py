def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False 
#print(contains("watermelon", "melon")) True
#print(contains("watermelon", "berry")) False


def common_letters(string_one, string_two):
    list= []
    for letter in string_one:
        if letter in string_two and not letter in list:
            list.append(letter)
    return list
print(common_letters("общение с мишей это когда ты минуту назад обсуждал овервотч" , 
"а теперь он кидает тебе видео с винстаном (персонажем-обезьяной)")) 