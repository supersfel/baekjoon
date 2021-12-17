from itertools import combinations
from itertools import permutations
N = int(input())
user =  [x for x in range(N)]
s = [list(map(int,input().split())) for _ in range(N)]
result = 9999

for start in combinations(user,N//2):
    if start[0] != 0:
        break

    link = []
    for i in user:
        if i not in start:
            link.append(i)

    start_point,link_point = 0,0
    for man in permutations(start,2):
        start_point += s[man[0]][man[1]]
    for man in permutations(link,2):
        link_point += s[man[0]][man[1]]

    point_gap = abs(start_point-link_point)
    if point_gap < result:
        result = point_gap

print(result)