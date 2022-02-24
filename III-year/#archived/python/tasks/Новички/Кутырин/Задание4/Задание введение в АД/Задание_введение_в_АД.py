import csv
import math
List = []

with open("Nedvig.csv") as File:  
    reader = csv.reader(File,delimiter=";")
    for i in reader:
        List.append(i)

"""
for i in List:
    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False
    if is_number(i[7])==True:
        List_prices.append(i[7])
    else:
        pass  

почему то не воспринимает float"""
  
List.pop(0)
List_prices = []

for i in List:
    try:
        List_prices.append(i[7])
    except:
        pass

print(List_prices)
print("max:",max(List_prices),"\n") 
print("min:",min(List_prices),"\n") # №1


def str_to_num(str):
    str = str.strip()
    if '.' in str and str.replace('.','').isdigit(): #если числа с "," то не работает
        return float(str)
    elif str.isdigit():
        return int(str)
num_list = []
for i in List_prices:
    n = str_to_num(i)
    if n is not None:
        num_list.append(str_to_num(i)) 
print(num_list)
print("average:",sum(num_list)/len(num_list),"\n")  # №2


price = [float(i[7]) for i in List] #если числа с "," то не работает
print(price)

price_counts = {}
for p in price:
    if p not in price_counts:
        price_counts[p] = 1
    else:
        price_counts[p] += 1
max_p = 0
mode = None
for k, v in price_counts.items():
    if max_p < v:
        max_p = v
        mode = k
print("mode:",mode,"times:", max_p,"\n") 


middle = math.ceil((len(price)/2))
sorted_price = sorted(price)
print(sorted_price)
print("median:",sorted_price[middle],"\n")  # №3

# №4-5



List_one_room = []
for i in List:
    for j in i:
        if i[2]=='1':
            List_one_room.append(i)
            break
        else:
            pass
print("One room \n",List_one_room,"\n")

price = [float(i[7]) for i in List_one_room]
print("average:",sum(price)/len(price),"\n")
price_counts = {}
for p in price:
    if p not in price_counts:
        price_counts[p] = 1
    else:
        price_counts[p] += 1
max_p = 0
mode = None
for k, v in price_counts.items():
    if max_p < v:
        max_p = v
        mode = k
print("mode:",mode,"times:", max_p,"\n") 
middle = math.ceil((len(price)/2))
sorted_price = sorted(price)
print("median:",sorted_price[middle],"\n")




List_two_room = []
for i in List:
    for j in i:
        if i[2]=='2':
            List_two_room.append(i)
            break
        else:
            pass
print("Two room \n",List_two_room,"\n")

price = [float(i[7]) for i in List_two_room]
print("average:",sum(price)/len(price),"\n")
price_counts = {}
for p in price:
    if p not in price_counts:
        price_counts[p] = 1
    else:
        price_counts[p] += 1
max_p = 0
mode = None
for k, v in price_counts.items():
    if max_p < v:
        max_p = v
        mode = k
print("mode:",mode,"times:", max_p,"\n") 
middle = math.ceil((len(price)/2))
sorted_price = sorted(price)
print("median:",sorted_price[middle],"\n")




List_four_room = []
for i in List:
    for j in i:
        if i[2]=='4':
            List_four_room.append(i)
            break
        else:
            pass
print("Four room \n",List_four_room,"\n")

price = [float(i[7]) for i in List_four_room]
print("average:",sum(price)/len(price),"\n")
price_counts = {}
for p in price:
    if p not in price_counts:
        price_counts[p] = 1
    else:
        price_counts[p] += 1
max_p = 0
mode = None
for k, v in price_counts.items():
    if max_p < v:
        max_p = v
        mode = k
print("mode:",mode,"times:", max_p,"\n") 
middle = math.ceil((len(price)/2))
sorted_price = sorted(price)
print("median:",sorted_price[middle],"\n")


# №6
def custom_key(string): 
    return string[7] 
List_one_room.sort(key=custom_key,reverse=True)
List_two_room.sort(key=custom_key,reverse=True)
List_four_room.sort(key=custom_key,reverse=True)
print(List_one_room,'\n')
print(List_two_room,'\n')
print(List_four_room,'\n')