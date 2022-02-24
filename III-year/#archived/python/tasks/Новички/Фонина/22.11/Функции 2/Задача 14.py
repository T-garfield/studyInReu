def game(pl1, pl2):
    if pl1 == "камень" and pl2 == "ножницы":
        return print("Игрок 1 победил")
    elif pl1 == "камень" and pl2 == "бумага":
        return print("Игрок 2 победил")
    elif pl1 == "ножницы" and pl2 == "бумага":
        return print("Игрок 1 победил")
    elif pl1 == "ножницы" and pl2 == "камень":
        return print("Игрок 2 победил")
    elif pl1 == "бумага" and pl2 == "ножницы":
        return print("Игрок 2 победил")
    elif pl1 == "бумага" and pl2 == "камень":
        return print("Игрок 1 победил")
    else:
        return print("Победила дружба ыыыы")
game("ножницы", "бумага")