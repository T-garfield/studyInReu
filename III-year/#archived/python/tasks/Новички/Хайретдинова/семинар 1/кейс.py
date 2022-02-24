Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price*Oil_work_time
Oil_price = 700*1.05

Filtr_work = 4500*0.5
Filtr_price = 300*1.05

Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price
Net_sum_cost = Cost_sum - Cost_sum * 0.03

print ('Расчет работ по представленному автомобилю:')
print (f'Замена масла (работы) - {Oil_work_cost} руб.')
print (f'Масло Castrol - {Oil_price} руб.')
print (f'Замена воздушного фильтра - {Filtr_work} руб.')
print (f'Воздушный фильтр - {Filtr_price} руб.')
print (f'Итого - {Cost_sum} руб.')
print ('Персональная скидка - 3%')
print (f'Итого с учетом скидки - {Net_sum_cost} руб.')
print ('Спасибо, что выбираете Нас!')
