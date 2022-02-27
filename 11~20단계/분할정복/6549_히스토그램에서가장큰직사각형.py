import sys
lst = list(map(int,sys.stdin.readline().split())) + [0]

while lst!=[0,0]:
    result = 0
    stack=[[0,0]]
    for i in range(1,lst[0]+2):
        while stack[-1][1] > lst[i]:
            tmp_lst = stack.pop()
            tmp_area = 0
            tmp_area = max((i-1-stack[-1][0]) * tmp_lst[1], tmp_lst[1])
            result = max(tmp_area,result)
        stack.append([i,lst[i]])

    print(result)
    lst =list(map(int,sys.stdin.readline().split())) + [0]