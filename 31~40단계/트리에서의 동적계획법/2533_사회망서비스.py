import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
tree = [ [] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
dp = [ [0,0] for _ in range(n+1) ]

def dfs(node):

    visited[node] = 1
    dp[node][1] = 1
    for i in tree[node]:
        if not visited[i]:
            dfs(i)
            dp[node][1] += min(dp[i][0],dp[i][1])
            dp[node][0] += dp[i][1]
dfs(1)
print(min(dp[1][0],dp[1][1]))