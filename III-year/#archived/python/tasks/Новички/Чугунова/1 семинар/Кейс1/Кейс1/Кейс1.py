Oil_work_price = 500;
Oil_work_time = 0.7;
Oil_work_cost = Oil_work_price * Oil_work_time;
Oil_price = 700 + ((700/100)*5);
Oil_work_price = 400;
Oil_work_time = 0.5;
Filtr_work = Oil_work_price * Oil_work_time;
Filtr_price = 300 + ((300/100) * 5);
Cost_sum = Oil_work_cost + Filtr_work + Oil_price + Filtr_price;
Net_sum_cost = Cost_sum - ((Cost_sum*3)/100);
print('Расчет работ по представленному автомобилю:\n'
      'Замена масла (работы).............', Oil_work_cost, '\n'
      'Масло Castrol...............................', Oil_price,'\n'
      'Замена воздушного фильтра....', Filtr_work,'\n'
      'Воздушный фильтр.....................',Filtr_price,'\n'
      'Итого...............................................',Cost_sum,'\n'
      'Персональная скидка....................................3%','\n'
      'Итого с учетом скидки................',Net_sum_cost,'\n'
      'Спасибо, что выбираете Нас!'
      )
