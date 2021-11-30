import sys

N = str(sys.stdin.readline())
n = str('100')
count = 0
a = N

if (int(N) < 10):
    N = '0' + N

while(int(a) != int(n)):
    n = str( int(N[0]) + int(N[1]))
    if (int(n) < 10):
        n = '0' + n

    n = N[1] + n[1]
    N = n
    count +=1

print(count)
