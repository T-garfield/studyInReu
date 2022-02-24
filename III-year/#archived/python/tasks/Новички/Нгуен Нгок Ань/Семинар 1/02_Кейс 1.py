Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price * Oil_work_time

Oil_price_buy = 700
Oil_price = Oil_price_buy * 1.05

Filtr_work_price = 450
Filtr_work_time = 0.5
Filtr_work = Filtr_work_price * Filtr_work_time

Filtr_price_buy = 300
Filtr_price = Filtr_price_buy * 1.05

Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price
Discount = 0.03
Net_sum_cost = Cost_sum * (1-Discount)

print("Расчет работ по представленному автомобилю:")
print("Замена масла (работы)……………………",int(Oil_work_cost),"руб.")
print("Масло Castrol…………………………………………",int(Oil_price),"руб.")
print("Замена воздушного фильтра…………",int(Filtr_work),"руб.")
print("Воздушный фильтр…………………………………",int(Filtr_price),"руб.")
print("Итого……………………………………………………………",int(Cost_sum),"руб.")
print("Персональная скидка………………………………",int(Discount*100),"%",)
print("Итого с учетом скидки…………………",int(Net_sum_cost),"руб.")