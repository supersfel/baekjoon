t = int(input())

sc = list(map(int,input().split()))

sum = 0

for a in sc:
    sum+= a/max(sc)  * 100

print(sum/t)