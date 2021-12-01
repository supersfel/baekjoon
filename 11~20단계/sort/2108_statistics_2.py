import sys
from collections import Counter
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

print(round(sum(lst)/len(lst)))#평균
lst.sort()
print(lst[len(lst)//2])#중앙값

c_lst=Counter(lst).most_common(2)
if len(lst) > 1:
    if c_lst[0][1] == c_lst[1][1]:
        print(c_lst[1][0])
    else:
        print(c_lst[0][0])
else:
    print(c_lst[0][0])

print(max(lst)-min(lst))#범위