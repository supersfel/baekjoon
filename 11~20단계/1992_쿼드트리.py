n= int(input())

lst = [ input() for _ in range(n)]
result=''

def f(x,y,n):
    num = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j] != num:
                print('(',end='')
                f(x,y,n//2)
                f(x, y + n // 2, n // 2)
                f(x+n//2,y,n//2)
                f(x+n//2,y+n//2,n//2)
                print(')',end='')
                return

    if num == '1':
        print('1',end='')
    else:
        print('0',end='')
f(0,0,n)
