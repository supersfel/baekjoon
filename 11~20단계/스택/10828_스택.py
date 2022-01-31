import sys
n = int(input())
lst = []

for _ in range(n):
    order = sys.stdin.readline().strip()

    if order == 'pop':
        if len(lst)==0:
            print(-1)
        else:
            print(lst.pop())
    elif order == 'size':
        print(len(lst))
    elif order == 'empty':
        if len(lst)==0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[-1])
    else:
        lst.append(order[5:])


