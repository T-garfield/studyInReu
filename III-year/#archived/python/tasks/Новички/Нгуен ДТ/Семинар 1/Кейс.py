oil_work_price = 500
oil_work_time = 0.7
oil_work_cost = oil_work_price * oil_work_time
oil_price = 700 * 5 / 100
filtr_work = 450 * 0.5
filtr_price = 300 * 5 / 100
cost_sum = oil_work_cost + oil_price + filtr_price + filtr_work
sale = cost_sum * 3 / 100
net_sum_cost = cost_sum - sale
print('Расчет работ по представленному автомобилю:')
print('Замена масла (работы) ', oil_work_cost, 'руб')
print('Значение переменной ', oil_price, 'руб')
print('Масло Castrol ', oil_price, 'руб')
print('Замена воздушного фильтра ', filtr_work, 'руб')
print('Воздушный фильтр ', filtr_price, 'руб')
print('Итого ', cost_sum, 'руб')
print('Персональная скидка 3% ', sale, 'руб')
print('Итого с учетом скидки ', net_sum_cost, 'руб')
