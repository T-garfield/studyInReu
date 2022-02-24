#Матвеев
Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price*Oil_work_time
Oil_price = 700 * 1.05

Filtr_work_price = 450
Filtr_work_time = 0.5
Filtr_work_cost = Filtr_work_price*Filtr_work_time
Filtr_price = 300*1.05
Cost_sum = Oil_work_cost + Oil_price + Filtr_work_cost + Filtr_price
Net_sum_cost = Cost_sum*0.97

print('Расчет работ по представленному автомобилю:')
print('Замена масла (работы)',Oil_work_cost)
print('Масло Castrol',Oil_price)
print('Замена воздушного фильтра',Filtr_work_cost)
print('Воздушный фильтр',Filtr_price)
print('Итого',Cost_sum)
print('Персональная скидка = 3%')
print('Итого с учетом скидки',Net_sum_cost)
print('Спасибо, что выбираете Нас!')