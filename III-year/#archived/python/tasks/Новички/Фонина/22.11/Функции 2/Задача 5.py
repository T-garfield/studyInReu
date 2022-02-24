def film (rating):
    if rating <= 5:
        return print("ИЗБЕГАТЬ ЛЮБОЙ ЦЕНОЙ!!!!!!!")
    elif rating < 9:
        return print("это было весело :)")
    else:
        return print("Отлично!")
(film(10))
# если на строке 8 написать print(film(6)), 
# то ниже результата выполнения функции будет писать 'none'
# а нам такое не надо!!