t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(float,input().split())
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5

    if d==0 and r1==r2:
        print(-1)
    elif d == abs(r2-r1) or d == r1 + r2:
        print(1)

    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)
    else:
        print(0)