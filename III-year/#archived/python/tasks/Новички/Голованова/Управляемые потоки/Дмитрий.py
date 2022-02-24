'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
user_name="Дмитрий"
Dmitriy_check= "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome="Добро пожаловать "
if user_name=="Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome+user_name)

user_name="Ангелина"
if user_name=="Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome+user_name)