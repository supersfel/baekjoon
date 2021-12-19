from itertools import product
import sys
lst = [[[1]*21]*21]*21
print(lst)
numbers = [x for x in range(1,11)]



for num in product(numbers,repeat=3):

    a,b,c = num[0],num[1],num[2]
    print(lst[1][1][1])
    if b>=a or c >=a:
        lst[a][b][c] = 2**a
    else:

        lst[a][b][c] = lst[a-1][b][c] + lst[a-1][b-1][c] + lst[a-1][b][c-1] - lst[a-1][b-1][c-1]
        print('----------')
        print(lst[a-1][b][c])
        print(lst[a - 1][b-1][c])
        print(lst[a - 1][b][c-1])
        print(lst[a - 1][b-1][c-1])
        print('----------')
    print(a,b,c,':',lst[a][b][c])



def w(a,b,c):
    if a>20 or b > 20 or c > 20:
        return lst[20][20][20]
    else:
        return lst[a][b][c]

print(lst)


while True:
    a,b,c = map(int,sys.stdin.readline().split())
    print("w(%d,%d,%d) = %d"%(a,b,c,w(a,b,c)))
    if a==-1 and b ==-1 and c==-1:
        break



