#зад_3
list1 = ['a','b','c']
list2 = ['x','y','z']

c=[]
for i, j in zip(list1,list2):
	c.append([i,j])
print(c)