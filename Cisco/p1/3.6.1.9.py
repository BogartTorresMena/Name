my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp=[]

for i in my_list:
    if i not in temp:
        temp.append(i)

my_list=temp[:]

print("La lista con elementos únicos:")
print(my_list)
