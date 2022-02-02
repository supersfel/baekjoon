t = int(input())

for _ in range(t):
    lst = []
    for i in input():
        if i=='(':
            lst.append(i)
        elif len(lst)==0:
            lst.append(i)
            break
        else:
            lst.pop()
    print('YES' if len(lst)==0 else 'NO')

