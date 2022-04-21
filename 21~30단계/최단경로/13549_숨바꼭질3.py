import sys
from collections import deque

M = 100000


def bfs():
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()
        if now == K:
            return cnt[now]

        # 1
        # x = now
        # while 0 < x <= M:
        #     if cnt[x] == -1:
        #         cnt[x] = cnt[now]
        #         q.appendleft(x)
        #     x *= 2

        # 2
        if 2 * now <= M and cnt[2 * now] == -1:
            cnt[2 * now] = cnt[now]
            q.appendleft(2 * now)
        ##################################

        for i in (now - 1, now + 1):
            if 0 <= i <= M and cnt[i] == -1:
                cnt[i] = cnt[now] + 1
                q.append(i)


N, K = map(int, sys.stdin.readline().split())
cnt = [-1] * (M + 1)
cnt[N] = 0
if K <= N:
    print(N - K)
else:
    print(bfs())