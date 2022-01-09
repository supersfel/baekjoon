import sys
n,k = map(int,sys.stdin.readline().split())
coin = [ 0 ]
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

count = 0
for i in range(n,0,-1):
    count += (k // coin[i])
    k = k % coin[i]

print(count)

