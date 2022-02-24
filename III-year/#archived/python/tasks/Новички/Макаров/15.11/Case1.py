Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price * Oil_work_time
Oil_price = 700*0.05 + 700
Filtr_work = 450 * 0.5 
Filtr_price = 300 * 0.05 + 300
Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price
Net_sum_cost = Cost_sum * 0.03
print("Расчет по предоставленному автомобилю:")
a = "Замена масла(работы)................"
print(a,Oil_work_cost)
b = "Масло Castrol......................."
print(b,Oil_price)
work = "Замена воздушного фильтра..........."
print(work,Filtr_work)
price = "Воздушный фильтр...................."
print(price,Filtr_price)
Final = "Итого..............................."
print(Final,Cost_sum)
Discount = "Персональная скидка................. 3%"
print(Discount)
FinalD = "Итого с учетом скидки .............."
print(FinalD,Net_sum_cost)
print("Спасибо,что выбираете нас!")




