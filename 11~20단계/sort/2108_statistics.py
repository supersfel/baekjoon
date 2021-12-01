import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

print(round(sum(lst)/len(lst)))#평균
lst.sort()
print(lst[len(lst)//2])#중앙값

dic={}
for i in lst:
    dic[i] = lst.count(i)
max_cnt = sorted(list(dic.values()),reverse=True)[0]

m_lst= list (key for key,value in dic.items() if value == max_cnt)

print(m_lst[0] if len(m_lst)==1 else m_lst[1])

print(max(lst)-min(lst))#범위