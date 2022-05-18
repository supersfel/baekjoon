import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [ [0,0] for _ in range(n+1) ]
count = [ [[],[]] for _ in range(n+1)]
visited = [ False ] * (n+1)
def dfs(node):
    visited[node] = True
    dp[node][1] = w[node]
    count[node][1] += [node]
    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            dp[node][1] += dp[i][0]
            count[node][1]+=(count[i][0])
            if dp[i][0] > dp[i][1]:
                dp[node][0] += dp[i][0]
                count[node][0] += count[i][0]
            else:
                dp[node][0] += dp[i][1]
                count[node][0] += count[i][1]
dfs(1)
if dp[1][1] > dp[1][0]:
    print(dp[1][1])
    count[1][1].sort()
    print(*count[1][1])
else:
    print(dp[1][0])
    count[1][0].sort()
    print(*count[1][0])


