n = int(input())
lst = [ list(map(int,input().split())) for _ in range(n) ]
blue,white = 0,0

def f(x,y,n):
    global blue,white
    num = lst[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if num != lst[i][j]:
                f(x,y,n//2)
                f(x,y+n//2,n//2)
                f(x+n//2,y,n//2)
                f(x+n//2,y+n//2,n//2)
                return

    if num == 0:
        white +=1
        return
    else:
        blue +=1
        return
f(0,0,n)
print(white)
print(blue)
