maxnum = 0
N, M = map(int, input().split())
lst = list(map(int, input().split()))

for i in lst:
    for j in lst:
        for k in lst:
            if i == j or j == k or k == i:
                pass
            else:
                if maxnum < i+j+k <=M:
                    maxnum = i+j+k
print(maxnum)
