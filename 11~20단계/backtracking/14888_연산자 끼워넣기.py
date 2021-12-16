from itertools import permutations
import sys

n = int(sys.stdin.readline())
num_lst = list(map(int,sys.stdin.readline().split()))
cal = list(map(int,sys.stdin.readline().split()))

cal_lst=[]

for i,j in enumerate(cal):
    while(j != 0):
        cal_lst.append(i)
        j -=1


max_num,min_num = -1000000000,1000000000
for symbols in permutations(cal_lst):

    num=num_lst[0]

    for i in range(len(num_lst)-1):


        if symbols[i] == 0:
            num += num_lst[i+1]
        elif symbols[i] == 1:
            num -= num_lst[i + 1]
        elif symbols[i] == 2:
            num *= num_lst[i + 1]
        elif symbols[i] == 3:
            if num >0:
                num = num//num_lst[i + 1]
            else:
                num = -(-num//num_lst[i+1])

    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num

print(max_num)
print(min_num)


