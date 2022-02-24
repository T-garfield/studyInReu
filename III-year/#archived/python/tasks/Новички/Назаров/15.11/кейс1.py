Oil_work_price=500
Oil_work_time=0.7
Oil_work_cost=Oil_work_price*Oil_work_time
Oil_price=700*1.05
Filtr_work=450*0.5
Filtr_price=300*1.05
Cost_sum=Oil_work_cost+Oil_price+Filtr_work+Filtr_price
Net_sum_cost=Cost_sum*0.97
print('Расчет работ по представленному автомобилю:\n'
'Замена масла (работы):',Oil_work_cost, 'руб.\n'
'Масло Castrol:',Oil_price,'руб.\n'
'Замена воздушного фильтра:',Filtr_work,'руб\n'
f'Воздушный фильтр: {Filtr_price} руб\n'
f'Итого:{Cost_sum}руб\n'
'Персональная скидка: 3%\n'
f'Итого с учетом скидки: {Net_sum_cost}\n'
'Спасибо, что выбираете Нас!')
