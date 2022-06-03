import sys
input = sys.stdin.readline

n,m = map(int,input().split())

hear = set()
for _ in range(n):
    hear.add(input().strip())

see = set()
for _ in range(m):
    see.add(input().strip())

result = sorted(list(hear&see))
print(len(result))
for i in result:
    print(i)


