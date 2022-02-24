def games (win, lose):
    total = win + lose
    winning_ratio = (win/total)*100
    return winning_ratio
print ('Коэффициент выигрыша составляет ' + str(games(50,30)) + '%')