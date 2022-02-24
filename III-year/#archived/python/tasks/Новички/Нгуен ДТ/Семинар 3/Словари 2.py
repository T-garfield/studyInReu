# 1
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries" , "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["G emini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# 2
print()
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

# 3
print()
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha']=30
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Этот ключ не существует")

# 4
print()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# 5
print()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
user = list(user_ids.keys())
classes = list(num_exercises.keys())
print(user)
print(classes)

# 6
print()
total_exercises = ()
total_exercises = list(num_exercises.values())
print(total_exercises)

# 7
print()
tarot = {1:  "The Magician", 2:  "The High Priestess", 3:  "The Empress", 4: "The Emperor", 5: "The Hierophant", 6:  "The Lovers", 7:  "The Chariot ", 8: "Strength", 9:  "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12:  "The Hanged Man", 13: "Death", 14:  "Temperance", 15: "The Devil", 16:  "The Tower", 17:  "The Star", 18: "The Moon", 19: "The Sun", 20:  "Judgement", 21:  "The World", 22: "The Fool"}
spread = {}
spread["past"] = tarot.get(13)
spread["present"] = tarot.get(22)
spread["future"] = tarot.get(10)
print(spread)