import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()

for _ in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push_front' :
        que.appendleft(order[1])
    elif order[0] == 'push_back' :
        que.append(order[1])
    elif order[0] == 'pop_front':
        if len(que) ==0:
            print(-1)
        else:
            print(que.popleft())
    elif order[0] == 'pop_back':
        if len(que) == 0:
            print(-1)
        else :
            print(que.pop())
    elif order[0] =="size":
        print(len(que))
    elif order[0] == 'empty' :
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(que) ==0:
            print(-1)
        else :
            print(que[0])
    elif order[0] == 'back':
        if len(que) ==0:
            print(-1)
        else:
            print(que[-1])