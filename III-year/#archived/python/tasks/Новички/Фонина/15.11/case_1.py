Oil_work_price = 500

Oil_work_time = 0.7

Oil_work_cost = Oil_work_price * Oil_work_time

Oil_price = 700 + (700 * 0.05) #700 + 5%

Filtr_work_price = 450 * 0.5

Filtr_price = 300 + (300 * 0.05)

Cost_sum = Oil_price + Oil_work_price + Filtr_price + Filtr_work_price

Net_sum_cost = Cost_sum - (Cost_sum * 0.03)

print('Расчет работ по представленному автомобилю:')
print('Замена масла (работы): ', Oil_work_cost)
print('Масло Castrol: ', Oil_price)
print('Замена воздушного фильтра: ', Filtr_work_price)
print('Воздушный фильтр: ', Filtr_price)
print('Итого: ', Cost_sum)
print('Персональная скидка: 3%')
print('Итого с учетом скидки: ', Net_sum_cost)
