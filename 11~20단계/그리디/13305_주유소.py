import sys
n = int(sys.stdin.readline())
distance = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

num = price[0]
result = 0
for i in range(n-1):
    if price[i] < num:
        num = price[i]
    result += num * distance[i]

print(result)