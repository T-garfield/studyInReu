first_names = ['Ainsley', 'Ben', 'Chani', 'Deepak']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range (4)
name_and_age_and_ids = zip(first_names, all_ages, ids)
print(list(name_and_age_and_ids))