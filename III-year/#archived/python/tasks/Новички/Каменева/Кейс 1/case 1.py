Oil_work_price = 500
Oil_work_time = 0.7

Oil_work_cost = Oil_work_price * Oil_work_time

Oil_price = (700*5/100)+700  

Oil_work_price = 450
Oil_work_time = 0.5

Filtr_work = Oil_work_price * Oil_work_time

Filtr_price = (300*5/100)+300 

Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price

Net_sum_cost = Cost_sum - (Cost_sum*3/100)

print("Расчет работ по представленному автомобилю:")
print("Замена масла (работы)…………  ",Oil_work_cost, "руб.")
print("Масло Castrol…………………………",Oil_price, "руб.")
print("Замена воздушного фильтра…",Filtr_work, "руб.")
print("Воздушный фильтр………………… ",Filtr_price, "руб.")
print("Итого……………………………………… ",Cost_sum, "руб.")
print("Персональная скидка……………………………3%")
print("Итого с учетом скидки……………",Net_sum_cost, "руб.")

print ("Спасибо, что выбираете Нас!")