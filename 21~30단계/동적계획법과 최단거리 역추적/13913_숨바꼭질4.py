from collections import deque
n,k = map(int,input().split())
high = 100001
cnt = [ [-1 ,-1] for _ in range(high) ]
cnt[n][0] = 0
cnt[n][1] = n

def bfs(N):
    q = deque([N])
    while q:
        now = q.popleft()
        if now == k:
            return cnt[now][0]

        for next in (now*2,now+1,now-1):
            if 0 <= next < high and cnt[next][0] == -1:
                cnt[next][0] = cnt[now][0] + 1
                cnt[next][1] = now
                q.append(next)

bfs(n)
print(cnt[k][0])
tmp = k
result = []
while tmp != n:
    result.append(tmp)
    tmp = cnt[tmp][1]
result.append(n)
result.reverse()
print(*result)