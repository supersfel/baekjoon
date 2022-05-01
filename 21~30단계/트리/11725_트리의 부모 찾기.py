import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
tree = [ [] for _ in range(n + 1)]
parents =[ 0 for _ in range(n + 1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    for i in tree[node]:
        if parents[i] == 0:
            parents[i] = node
            dfs(i)
dfs(1)


print(*parents[2:],sep='\n')