import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
s_lst = sorted(set(lst))
result_lst = []
for i in lst:
    result_lst.append(s_lst.index(i))
for j in result_lst:
    print(j,end=' ')