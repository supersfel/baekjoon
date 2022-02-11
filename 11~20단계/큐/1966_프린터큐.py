t = int(input())
from collections import deque

for _ in range(t):
    n,m = map(int,input().split())
    que = deque(list(map(int,input().split())))
    count = 1

    for i in range(n):
        while ( que[0] < max(que)):
            que.append(que.popleft())
            if m==0:
                m=len(que)-1
            else:
                m -=1
        que.popleft()
        if m == 0:
            m = len(que)-1
            print(count)
            break
        else:
            m -= 1
        count += 1



