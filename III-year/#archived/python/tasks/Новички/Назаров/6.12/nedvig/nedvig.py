import pandas as pd


data = pd.read_csv('Nedvig.csv', encoding='1251', sep=';') 

data['Цена, тыс. руб.'] = [x.replace(',', '.') for x in data['Цена, тыс. руб.']]
data['Цена, тыс. руб.'] = data['Цена, тыс. руб.'].astype('float')

max = data['Цена, тыс. руб.'].max()
print(f'максимальная цена - {max}')       #1. Найти максимум и минимум

min = data['Цена, тыс. руб.'].min()
print(f'минимальная цена - {min}')

price_mean = data['Цена, тыс. руб.'].mean()     #2. Найти среднее значение
print(f'среднее значение - {price_mean}')

mediana = data['Цена, тыс. руб.'].median() 
print(f'медиана - {mediana}')                   #3. Найти моду и медиану

moda= data['Цена, тыс. руб.'].mode().values[0] 
print(f'мода - {moda}')


data_single_room = data.loc[data['Число комнат'] == 1]
data_two_room = data.loc[data['Число комнат'] == 2]           #4. Разделить набор данных на три отдельных набора данных по признаку квартир(отдельно однокомнатные, двухкомнатные, четырёхкомнатные)
data_four_room = data.loc[data['Число комнат'] == 4]

print(data_single_room)
print(data_two_room)
print(data_four_room)

#однокомнатные
max = data_single_room['Цена, тыс. руб.'].max()               #5. Рассчитать показатели из 1–4 пункта для каждого из наборов данных
print(f'максимальная цена однокомнатных - {max}')

min = data_single_room['Цена, тыс. руб.'].min()
print(f'минимальная цена - {min}')

price_mean = data_single_room['Цена, тыс. руб.'].mean() 
print(f'среднее значение - {price_mean}')

mediana = data_single_room['Цена, тыс. руб.'].median() 
print(f'медиана - {mediana}')

moda = data_single_room['Цена, тыс. руб.'].mode().values[0] 
print(f'мода - {moda}')


#двухкомнатные

max = data_two_room['Цена, тыс. руб.'].max()
print(f'максимальная цена двухкомнатных - {max}')

min = data_two_room['Цена, тыс. руб.'].min()
print(f'минимальная цена - {min}')

price_mean = data_two_room['Цена, тыс. руб.'].mean() 
print(f'среднее значение - {price_mean}')

mediana = data_two_room['Цена, тыс. руб.'].median() 
print(f'медиана - {mediana}')

moda = data_two_room['Цена, тыс. руб.'].mode().values[0] 
print(f'мода - {moda}')


#четырехкомнатные

max = data_four_room['Цена, тыс. руб.'].max()
print(f'максимальная цена четырехкомнатных - {max}')

min = data_four_room['Цена, тыс. руб.'].min()
print(f'минимальная цена - {min}')

price_mean = data_four_room['Цена, тыс. руб.'].mean() 
print(f'среднее значение - {price_mean}')

mediana = data_four_room['Цена, тыс. руб.'].median() 
print(f'медиана - {mediana}')

moda = data_four_room['Цена, тыс. руб.'].mode().values[0] 
print(f'мода - {moda}')



sorted_data = data.sort_values(by='Цена, тыс. руб.', ascending=False) #6. Отсортировать по убыванию цены
print(sorted_data)                      