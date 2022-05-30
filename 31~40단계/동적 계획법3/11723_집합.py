import sys
input = sys.stdin.readline
m = int(input())
S=0
for _ in range(m):
    order = input().rstrip()

    if order =="all":
        S = (1<<20)-1
    elif order =="empty":
        S = 0
    else:
        order,num = order.split()
        num = int(num)-1

        if order=="add":
            S |= (1<<num)
        elif order=="check":
                print(1 if S & (1<<num) else 0)
        elif order=="toggle":
            S ^= (1<<num)
        elif order=="remove":
            S &= ~(1<<num)