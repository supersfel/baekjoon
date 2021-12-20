import sys
lst = [[[0 for k in range(21)] for j in range(21)] for i in range(21)]


def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b > 20 or c > 20:
        return w(20,20,20)
    elif lst[a][b][c]:
        return lst[a][b][c]
    elif b>=a or c >=a: #추가한 부분
        lst[a][b][c] = 2 **a
        return lst[a][b][c]
    else:
        lst[a][b][c] = w(a-1,b,c) +w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return lst[a][b][c]



while True:
    a,b,c = map(int,sys.stdin.readline().split())

    if a==-1 and b ==-1 and c==-1:
        break
    print("w(%d,%d,%d) = %d" % (a, b, c, w(a, b, c)))



