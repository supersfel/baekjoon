import sys
import math
input = sys.stdin.readline

n = int(input())

lst = [  list(map(float,input().split()))  for _ in range(n)]
lst.append(lst[0])

result = 0
for i in range(n):
    result += (lst[i][0]*lst[i+1][1] - lst[i][1] * lst[i+1][0])

result = math.fabs(result *0.5)
print(round(result,2))