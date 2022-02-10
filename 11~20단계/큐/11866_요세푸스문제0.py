from collections import deque
n,k = map(int,input().split())

que = deque([x for x in range(1,n+1)])
result = []

while len(que)>0:
    for _ in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())


print('<'+(', '.join(str(x) for x in result)) + '>')