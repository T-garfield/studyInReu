print("#задание 1\n")
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], 
"fire": ["Aries", "Leo", "Sagittarius"], 
"earth": ["Taurus", "Virgo", "Capricorn"], 
"air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['fire'])
print("\n")

print("#задание 2\n")
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], 
"fire": ["Aries", "Leo", "Sagittarius"], 
"earth": ["Taurus", "Virgo", "Capricorn"], 
"air":["Gemini", "Libra", "Aquarius"]}
key_to_check = "energy"
if key_to_check in zodiac_elements:
    print(zodiac_elements["energy"])
#ничего не выдает
key_to_check = "energy"
try:
    print(zodiac_elements["energy"])
except KeyError:
    print("Вы ошибились, так не бывает (͡° ͜ʖ ͡°)")
print("\n")

print("#задание 3\n")
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha']=30
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("«Неизвестный уровень кофеина (͡๏̯͡๏)")
print("\n")

print("#задание 4\n")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = print(user_ids.get("teraCoder", 100000))
stack_id = print(user_ids.get("superStackSmash", 100000))
print("\n")

print("#задание 5\n")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops":22, "lists": 19, "classes": 18, "dictionaries": 18}
for users in user_ids.keys():
    print(users)
print("\n")
for classes in num_exercises.keys():
    print(classes)
print("\n")

print("#задание 6\n")
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
for total_exercises in num_exercises.values():
    print(total_exercises)
print("\n")

print("#задание 7\n")
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 
4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 
8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 
16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 
20: "Judgement", 21: "The World", 22: "The Fool"}
spread = {}
spread["past"] = tarot[13]
spread["present"] = tarot[22]
spread["future"] = tarot[10]
print(spread)
print("\n")