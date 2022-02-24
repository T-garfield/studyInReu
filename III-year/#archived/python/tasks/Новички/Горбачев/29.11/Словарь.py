#Словарь 1
print ("Введение в словарь")
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print (sensors)
print (num_cameras)
print ("")

print ("Создание словаря")
#Короче сделаю немного интеерснее, добавив польского
translator = {"mountain": ["orod", "góra"],
"bread": ["bass", "chleb"], "friend": ["mellon", "przyjaciel"], "horse": ["roch", "koń"]}
print (translator)
print ("")

print ("Добавить ключ")
animals_in_zoo = {}
animals_in_zoo ["zeBro"] = 8
animals_in_zoo ["Monke"] = 12
animals_in_zoo ["Dino"] = 0
print (animals_in_zoo)
print ("")

print ("Добавить несколько ключей")
ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
ser_ids.update ({"theLooper": 138475, "stringQueen": 85739})
print (ser_ids)
print ("")

print ("Перезаписать значения")
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
"Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners ["Best Picture"] = "Moonlight"
oscar_winners ["Supporting Actress"] = "Viola Davis"
print (oscar_winners)
print ("")

print ("Понимание словаря")
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print (drinks_to_caffeine)
print ("")

print ("Заключение")
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
plays ["Purple Haze"] = 1
plays ["Respect"] = 5
library = {"The Best Songs": [plays], "Sunday Feelings": {}}
print (plays)
print (library)
print ("")

#Словарь 2
print("Получить ключ")
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])
print ("")

print("Получите недействительный ключ")
zodiac_elements = {"energy": ["Not a Zodiac element"], "water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements ["energy"] = "Not a Zodiac element"
Not_a_Zodiac_element = "energy"
if Not_a_Zodiac_element in zodiac_elements: print (zodiac_elements ["energy"])
print ("")

print("Try/Except для получения ключа")
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha']=30
try: 
    print(caffeine_level['matcha'])
except KeyError:
    print("Неизвестный уровень кофеина")
print("")

print("Безопасно получить ключ")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
print("")

print("Получить все ключи")
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
print("----------Users----------")
for users in user_ids.keys():
 print(users)
print("----------Lessons----------")
for lessons in num_exercises.keys():
 print(lessons)
print("")

print("Получить все значения")
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
for total_exercises in num_exercises.values():
 print(total_exercises)
print("")

print("Получить все предметы")
spread = {}
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}
Past = tarot.get(13)
Countinious = tarot.get(22)
Future = tarot.get(10)
spread[Past] = "прошедшее"
spread[Countinious] = "настоящее"
spread[Future] = "будущее"
print(spread)