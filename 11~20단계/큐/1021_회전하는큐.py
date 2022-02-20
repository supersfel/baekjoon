from collections import deque
n,m = map(int,input().split())
lst = list(map(int,input().split()))
que = deque([x for x in range(1,n+1)])
count = 0

for num in lst:
    if que.index(num) <= len(que)//2 :
        while(que[0]!=num):
            que.append(que.popleft())
            count +=1
    else:
        while(que[0]!=num):
            que.appendleft(que.pop())
            count +=1
    que.popleft()
print(count)
