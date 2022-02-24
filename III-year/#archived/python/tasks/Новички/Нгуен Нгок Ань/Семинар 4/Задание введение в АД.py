import pandas as pd

df = pd.read_csv('nedvig.csv', delimiter = ';', decimal=",")
print("1. Найти максимум и минимум")

sort_des = df.sort_values(by='Цена, тыс. руб.', ascending=False)
print("МАКСИМУМ")
print(sort_des.head(1))

sort_asc = df.sort_values(by='Цена, тыс. руб.', ascending=True)
print("\nМИНИМУМ")
print(sort_asc.head(1))

print("\n2. Найти среднее значение")
df['Цена, тыс. руб.'] = pd.to_numeric(df['Цена, тыс. руб.'], downcast='float')
mean = df['Цена, тыс. руб.'].mean()
print(mean, "тыс. руб.")

print("\n3. Найти моду и медиану")
mod = df['Цена, тыс. руб.'].mode()
if mod.count() == 1:
    print("Мода =", float(mod), "тыс. руб.")
else:
    print("Не имеет моды")

med = df['Цена, тыс. руб.'].median()
print("Медиана =", float(med), "тыс. руб.")

print("\n4. Разделить набор данных на три отдельных набора данных по признаку квартир (отдельно однокомнатные, двухкомнатные, четырёхкомнатные)")
print("ОДНОКОМНАТНЫЕ КВАРТИРЫ")
df1 = df[df['Число комнат'] == 1]
print(df1)

sort_des = df1.sort_values(by='Цена, тыс. руб.', ascending=False)
print("\nМАКСИМУМ")
print(sort_des.head(1))

sort_asc = df1.sort_values(by='Цена, тыс. руб.', ascending=True)
print("\nМИНИМУМ")
print(sort_asc.head(1))

mean1 = df1['Цена, тыс. руб.'].mean()
print("\nСреднее значение =", mean1, "тыс. руб.")

mod1 = df1['Цена, тыс. руб.'].mode()
if mod1.count() == 1:
    print("Мода =", float(mod1), "тыс. руб.")
else:
    print("Не имеет моды")

med1 = df1['Цена, тыс. руб.'].median()
print("Медиана =", float(med1), "тыс. руб.")

print("\nДВУХКОМНАТНЫЕ КВАРТИРЫ")
df2 = df[df['Число комнат'] == 2]
print(df2)

sort_des = df2.sort_values(by='Цена, тыс. руб.', ascending=False)
print("\nМАКСИМУМ")
print(sort_des.head(1))

sort_asc = df2.sort_values(by='Цена, тыс. руб.', ascending=True)
print("\nМИНИМУМ")
print(sort_asc.head(1))

mean2 = df2['Цена, тыс. руб.'].mean()
print("\nСреднее значение =", mean2, "тыс. руб.")

mod2 = df2['Цена, тыс. руб.'].mode()
if mod2.count() == 1:
    print("Мода =", float(mod2), "тыс. руб.")
else:
    print("Не имеет моды")

med2 = df2['Цена, тыс. руб.'].median()
print("Медиана =", float(med2), "тыс. руб.")

print("\nЧЕТЫРЕХКОМНАТНЫЕ КВАРТИРЫ")
df4 = df[df['Число комнат'] == 4]
print(df4)

sort_des = df4.sort_values(by='Цена, тыс. руб.', ascending=False)
print("\nМАКСИМУМ")
print(sort_des.head(1))

sort_asc = df4.sort_values(by='Цена, тыс. руб.', ascending=True)
print("\nМИНИМУМ")
print(sort_asc.head(1))

mean4 = df4['Цена, тыс. руб.'].mean()
print("\nСреднее значение =", mean4, "тыс. руб.")

mod4 = df4['Цена, тыс. руб.'].mode()
if mod4.count() == 1:
    print("Мода =", float(mod4), "тыс. руб.")
else:
    print("Не имеет моды")

med4 = df4['Цена, тыс. руб.'].median()
print("Медиана =", float(med4), "тыс. руб.")

print("\n6. Отсортировать по убыванию цены")
sort_des = df.sort_values(by='Цена, тыс. руб.', ascending=False)
print(sort_des)