lst = list(map(int,input().split()))

n = len(set(lst))

if n==1:
    print(1000 * lst[0] + 10000)
elif n == 2:
    if lst[0] == lst[1]:
        print(100*lst[0] + 1000)
    else:
        print(100*lst[2] + 1000)
else:
    print(max(lst)*100)

