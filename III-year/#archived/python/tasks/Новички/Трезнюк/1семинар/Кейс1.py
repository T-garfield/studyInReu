#Трезнюк Роман 4310БИ
Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price * Oil_work_time
Oil_price = 700 * 1.05

Filtr_work_price = 450
Filtr_work_time = 0.5
Filtr_work = Filtr_work_price * Filtr_work_time
Filtr_price = 300 * 1.05

Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price
discount = 0.03
Net_sum_cost = Cost_sum * (1 - 0.03)

print(f'Замена масла(работы)...........{Oil_work_cost} руб.')
print(f'Масло Castrol...........{Oil_price} руб.')
print(f'Замена воздушного фильтра...........{Filtr_work} руб.')
print(f'Воздушный фильтр...........{Filtr_price} руб.')
print(f'Итого...........{Cost_sum} руб.')
print(f'Персональная скидка...........{int(discount*100)} %')
print(f'Итого с учетом скидки...........{Net_sum_cost}')
print("Спасибо, что выбираете нас!")
