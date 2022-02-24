'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome = "Добро пожаловать "
user_name="Дмитрий"
АРМ1="Дмитрий"
АРМ2="Ангелина"
АРМ3="Василий"
АРМ4="Екатерина"
APM=АРМ4
if user_name=="Дмитрий" and APM!="Дмитрий":
    print(Dmitriy_check)
    if APM==user_name:
        print(welcome+user_name)
    else:
        print("Логин или пароль не верный, попробуйте еще раз")
