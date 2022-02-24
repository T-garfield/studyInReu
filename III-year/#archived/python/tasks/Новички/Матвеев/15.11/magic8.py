#Матвеев
import random

name = 'Саша'
question = 'Мне стоит делать сегодня домашку по питону?'
answer = ''
random_number = random.randint(1,9)
if random_number == 1:
	answer = 'Да, безусловно.'
elif random_number == 2:
	answer = 'Очень сомнительно.'
elif random_number == 3:
	answer = 'Это решительно так.'
elif random_number == 4:
	answer = 'Без сомнения.'
elif random_number == 5:
	answer = 'Ответ туманный, попробуйте еще раз.'
elif random_number == 6:
	answer = 'Спросите еще раз позже.'
elif random_number == 7:
	answer = 'Лучше не говорить вам сейчас.'
elif random_number == 8:
	answer = 'Мои источники говорят «нет».'
elif random_number == 9:
	answer = 'Прогноз не очень хороший.'
else:
   print('Ошибка')

print(name, 'Спрашивает:', question)
print('Магический шар отвечает:', answer)