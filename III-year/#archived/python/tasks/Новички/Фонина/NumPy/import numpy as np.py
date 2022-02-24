import numpy as np
#1
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
#2
B = A.copy()
print(B)
#3
A = np.zeros((2, 3))
print(A)
B = np.ones((3, 2))
print(B)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.zeros_like(A)
print(B)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.ones_like(A)
print(B)
#4
A = np.eye(3)
print(A)
#5
From = 2.5
To = 7
Step = 0.5
A = np.arange(From, To, Step)
print(A)
A = np.arange(5)
print(A)
A = np.arange(10, 15)
print(A)
A = np.zeros((2, 3), 'int')
print(A)
B = np.ones((3, 2), 'complex')
print(B)
A = np.ones((3, 2))
B = A.astype('str')
print(B)
print(np.sctypes)

#Доступ к элементам, срезы
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A[1, 1])
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A[1])
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A[1][1])
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A[1, :])
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A[:, 1])
A = np.arange(5)
print(A)
print(A[-1])
A = np.arange(5)
print(A)
print(A[[0, 1, -1]])
A = np.arange(5)
print(A)
print(A[0:4:2])
A = np.arange(5)
print(A)
print(A[0:4])
A = np.arange(5)
print(A)
print(A[:4])
A = np.arange(5)
print(A)
print(A[-3:])
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A[:, ::-1]
print("A", A)
print("B", B)
print(A)
B[0, 0] = 0
print(A)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.copy()[:, ::-1]
print("A", A)
print("B", B)
A = np.array([[1, 2, 3], [4, 5, 6]])
I = np.array([[False, False, True], [ True, False, True]])
print(A[I])
A = np.array([[1, 2, 3], [4, 5, 6]])
I = np.array([[False, False, True], [ True, False, True]])
A[I] = 0
print(A)
A = np.array([[1, 2, 3], [4, 5, 6]])

I1 = np.array([[False, False, True], [True, False, True]])
I2 = np.array([[False, True, False], [False, False, True]])

B = A.copy()
C = A.copy()
D = A.copy()

B[np.logical_and(I1, I2)] = 0
#True if both the operands are true
#false и fasle это false
#true и fasle это false
#false и true это false
#true и true это true
C[np.logical_or(I1, I2)] = 0
#True if either of the operands is true
#false и fasle это false
#true и fasle это true
#false и true это true
#true и true это true
D[np.logical_not(I1)] = 0
#True if an operand is false (complements the operand)
print('B\n', B)
print('\nC\n', C)
print('\nD\n', D)
#logical_and и logical_or принимают 2 операнда, logical_not — один
A = np.array([[1, 2, 3], [4, 5, 6]])

I1 = np.array([[False, False, True], [True, False, True]])
I2 = np.array([[False, True, False], [False, False, True]])

A[I1 & (I1 | ~ I2)] = 0
#первое действие - 0 2 0 0 0 0
#второе действие 1 2 0 0 5 0
print(A)
A = np.array([[1, 2, 3], [4, 5, 6]])
print('A before\n', A)

I = A > 3
print('I\n', I)

A[np.logical_or(A < 2, A > 4)] = 0
print('A after\n', A)

#Форма массива и ее изменение

A = np.arange(24)
B = A.reshape(4, 6)
C = A.reshape(4, 3, 2) #кол-во блоков, кол-во строк в одном, кол-во элементов в одной строке в одном
print('B\n', B)
print('\nC\n', C)
#размер вдоль каждой оси — shape 
#Функция reshape() изменяет форму массива без изменения его данных
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.ravel())
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.reshape(3, 2))
#x= A.reshape(1, 6, 1)
#print(x)
A = np.arange(24)
B = A.reshape(4, -1)
C = A.reshape(4, -1, 2)
print(B.shape, C.shape) #размер вдоль каждой оси — shape
A = np.array([[1, 2, 3], [4, 5, 6]])
B = A.reshape(-1) #Можно reshape использовать вместо ravel
print(B.shape)
