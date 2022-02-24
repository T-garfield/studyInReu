#1
def num(base,exp):
    mult=base**exp
    if mult>5000:
        return True
    else:
        return False
print(num(1,55))
#2
def range(num,low,high):
    if num>=low and num<=high:
        return True
    return False
print(range(5,1,9))
#3
def comp(your_name,my_name):
    if your_name==my_name:
        return True
    return False
print(comp('Jack','Jack'))
#4
def func(num):
    if num>100 and num<100:
        return True
    return False
print(func(1))
#5
def review(rating):
    if rating<=5:
        return 'Избегать любой ценой!'
    elif rating<9:
        return 'Это было весело'
    else:
        return 'Отлично!'
print(review(0))
#6
def compare(num1, num2, num3):
    if num2<num1 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    elif num3>num1 and num3>num2:
        return num3  
    elif num1==num2 or num2==num3 or num1==num3:
        return "Ничья!"
print(compare(5,5,5))

#7
def tenth_power(num):
    return num**10
def square_root(num):
    return num**(1/2)
print(tenth_power(2), square_root(36))

#8
def winrate(win, loss):
    perc=win/(win+loss)*100
    print(perc)
winrate(55,45)
    
#9
def avg(num1,num2):
    return (num1+num2)/2
print(avg(51,7))

#10
def ost(num1,num2):
   return num1%num2
print(ost(5,2))

#11
def twothreemult(num):
    print(num)
    print(num*2)
    print(num*3)
    return num*3

#11
def tips(total,tips_perc):
    return total*tips_perc/100
print(tips(1323,10))
#12
def f(x):
    if x<=-2:
        return 1-(x + 2)**2
    elif -2<x<=2:
        return -x/2
    else: 
        return (x - 2)**2+1
print(f(13))
#13
def calc(num1,num2, operation):
    if num2==0 and operation=='/':
         return ZeroDivisionError
    elif operation=='+':
        return num1+num2
    elif operation=='-':
         return num1-num2
    elif operation=='*':
         return num1*num2 
    elif operation=='/':
         return num1/num2
    else:
        return 'try again'
print(calc(2,0,'/'))
#14
def game(player1, player2):
    if player1=='камень':
        if player2=='бумага':
            return 'победил 2'
        else:
            return 'победил 1'
    elif player1=='ножницы':
        if player2=='камень':
            return 'победил 2'
        else:
            return 'победил 1'
    elif player1=='бумага':
        if player2=='ножницы':
            return 'победил 2'
        else:
            return 'победил 1'
print(game('камень', 'ножницы'))