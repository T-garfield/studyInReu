print("№1")
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], 
"fire": ["Aries", "Leo", "Sagittarius"], 
"earth": ["Taurus", "Virgo", "Capricorn"], 
"air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['fire'])
print("...............................")

print("№2")
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
    print("Вы ошибились, так не бывает")
print("....................................")

print("№3")
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha']=30
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")
print(".....................................................")

print("№4")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = print(user_ids.get("teraCoder", 100000))
stack_id = print(user_ids.get("superStackSmash", 100000))
print(".......................................")

print("№5")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops":22, "lists": 19, "classes": 18, "dictionaries": 18}
for users in user_ids.keys():
    print(users)
for classes in num_exercises.keys():
    print(classes)
print("....................................")

print("№6")
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
for total_exercises in num_exercises.values():
    print(total_exercises)
print("....................................................")

print("№7")
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
print("..............................................................")
