import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
b,c = map(int,input().split())

result = 0

for i in A:
    if b>=i:
        result += 1
    else:
        i=i-b
        if i % c == 0:
            result += i // c +1
        else:
            result += i // c + 2
print(result)
