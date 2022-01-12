import re
lst =[]

n = input()
num_lst = re.split('[+-]',n)

for i in n:
    if i== '-' or i == '+':
        lst.append(i)

pm = '+'
for i in range(len(lst)):
    if lst[i] == '-':
        pm = '-'
    lst[i] = pm

result = int(num_lst[0])
for i in range(len(lst)):
    if lst[i] == '+':
        result += int(num_lst[i+1])
    else:
        result -= int(num_lst[i+1])


print(result)