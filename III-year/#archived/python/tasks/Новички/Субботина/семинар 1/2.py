#кейс
oil_work_price = 500
oil_work_time = 0.7
oil_work_cost = oil_work_price * oil_work_time
oil_price = 700 * 1.05
filtr_work_price = 450
filtr_work_time = 0.5
filtr_work = filtr_work_price * filtr_work_time
filtr_price = 300 * 1.05
cost_sum = oil_work_cost + oil_price + filtr_work + filtr_price
net_sum_cost = cost_sum - cost_sum * 0.03
print(f"Цена без скидки:{cost_sum}")
print(f"Цена со скидкой:{net_sum_cost}")