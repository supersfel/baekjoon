from collections import deque
import sys

t = int(sys.stdin.readline())



for _ in range(t):
    flag = False
    order = sys.stdin.readline()
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline()[1:-2].split(',')

    if lst[0] != '':
        lst = deque(lst)
    else:
        lst = deque()

    d_flag = True

    for i in order:
        if i == 'R':
            if d_flag:
                d_flag=False
            else:
                d_flag=True
        elif i =='D':
            if len(lst) ==0:
                print('error')
                flag = True
                break

            if d_flag:
                lst.popleft()
            else:
                lst.pop()

    if order.count('R') %2 !=0:
        lst.reverse()

    if not flag:
        print('[',end='')
        for i in range(len(lst)):
            print(lst[i],end='')
            if i!= len(lst)-1:
                print(',',end='')
        print(']')