N = int(input())
lst =[1,2]

for i in range(2,N):
    lst.append((lst[0]+lst[1])%15746)
    lst.pop(0)
print(lst[0] if N==1 else lst[1] )


# 1 : 1 > 1 + 0
# 2 : 2 > 1 + 1
# 3 : 3 > 1 + 2 + 0
# 4 : 5 > 1 + 3 + 1
# 5 : 8 > 1 + 4 + 3 + 0
# 6 : 13 > 1 + 5 + 6 + 1
# 7 : 21 > 1 + 6 + 10 + 4

