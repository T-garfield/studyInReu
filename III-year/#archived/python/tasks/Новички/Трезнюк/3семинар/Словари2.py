#Задание 1
from typing import Match


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["water"])
print(zodiac_elements["fire"])
#Задание 2
#print(zodiac_elements["energy"]) - KeyError
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"]) # Ошибки нет
#Задание 3
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha'] = 30
try:
    print(caffeine_level['matcha'])
except:
    print("Неизвестный уровень кофеина")
#Задание 4
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
#Задание 5
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops":
22, "lists": 19, "classes": 18, "dictionaries": 18}
dict_keys = user_ids.keys()
users = dict_keys
dict_keys = num_exercises.keys()
classes = dict_keys
print(users)
print(classes)
#Задание 6
total_exercises = 0
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops":
22, "lists": 19, "classes": 18, "dictionaries": 18}
for item in num_exercises.values():
    total_exercises += item
print(total_exercises)
#Задание 7
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress",
4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}
spread = {}
spread["Past"] = tarot.get(13)
spread["Presence"] = tarot.get(22)
spread["Future"] = tarot.get(10)
print(spread)