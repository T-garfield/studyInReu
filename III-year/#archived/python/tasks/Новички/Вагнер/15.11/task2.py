Oil_work_price = 500
Oil_work_time = 0.7
Oil_work_cost = Oil_work_price*Oil_work_time
Oil_price = 700*1.05
Filtr_work = 4500*0.5
Filtr_price = 300*1.05
Cost_sum = Oil_work_cost + Oil_price + Filtr_work + Filtr_price
Net_sum_cost = Cost_sum - Cost_sum * 0.03
print(f"Цена без скидки:{Cost_sum}")
print(f"Цена со скидкой:{Net_sum_cost}")
