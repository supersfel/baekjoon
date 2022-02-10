import sys
n = int(sys.stdin.readline())

n_lst = [ x for x in range(n,0,-1)]
lst = [0]
result = []
try :
    for _ in range(n):
        num = int(sys.stdin.readline())

        if lst[-1]<num:
            while ( lst[-1] < num ):
                lst.append(n_lst.pop())
                result.append('+')
        else :
            while(lst[-1] > num):
                lst.pop()
                result.append('-')
        lst.pop()
        result.append('-')
    for i in result:
        print(i)
except :
    print('NO')




