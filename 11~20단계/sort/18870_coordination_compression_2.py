import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
s_lst = sorted(set(lst))
dic = {s_lst[i] : i for i in range(len(s_lst))}
for j in lst:
    print(dic[j],end=' ')