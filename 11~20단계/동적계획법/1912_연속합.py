import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
result = [lst[0]]

for i in range(n-1):
    result.append(max(result[i] + lst[i+1], lst[i+1] ))

print(max(result))
