import sys
from collections import deque
input = sys.stdin.readline

gear = [0]+[ deque([ int(x) for x in input().strip() ]) for _ in range(4)]
k = int(input())
orders = [ list(map(int,input().split())) for _ in range(k)]


def rotate(num,order):
    if order:
        if order == 1:
            gear[num].appendleft(gear[num].pop())
        else:
            gear[num].append(gear[num].popleft())

def process(order):
    num,odr = order
    visited[num] = odr
    if 1<=num-1<5 and not visited[num-1] and gear[num-1][2] != gear[num][6]:
        process([num-1,odr*(-1)])
    if 1<=num+1<5 and not visited[num+1] and gear[num+1][6] != gear[num][2]:
        process([num+1,odr*(-1)])

for order in orders:
    visited = [0] * 5
    process(order)
    for i in range(1,5):
        rotate(i,visited[i])

result = 0
for i in range(1,5):
    if gear[i][0]:
        result += 2**(i-1)
print(result)
