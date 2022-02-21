import sys
n = int(sys.stdin.readline())
minus,zero,plus = 0,0,0
lst = [ list(map(int,sys.stdin.readline().split())) for _  in range(n) ]

def f(x,y,n):
    global minus,zero,plus
    num = lst[x][y]


    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j] != num:
                f(x, y, n //3)
                f(x, y+ n//3, n // 3)
                f(x, y+ n//3+ n//3, n // 3)
                f(x+ n//3, y, n // 3)
                f(x+ n//3, y+ n//3, n // 3)
                f(x+ n//3, y+ n//3+ n//3, n // 3)
                f(x+ n//3+ n//3, y, n // 3)
                f(x+ n//3+ n//3, y+ n//3, n // 3)
                f(x + n // 3 + n // 3, y+ n//3+ n//3, n // 3)
                return
    if num == 1:
        plus +=1
    elif num == 0 :
        zero +=1
    else:
        minus +=1

f(0,0,n)
print(minus)
print(zero)
print(plus)