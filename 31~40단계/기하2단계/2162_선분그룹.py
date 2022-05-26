import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    tmp = x1 * y2 + x2 * y3 + x3*y1 -( y1*x2 + y2 * x3 + y3 * x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0
def check(a,b):
    x1,y1,x2,y2 = a
    x3,y3,x4,y4 = b

    answer = False
    if (ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)) == 0 and (
            ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)) == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3,
                                                                                                            y4) <= max(
                y1, y2):
            answer = True
    elif (ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)) <= 0 and (
            ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)) <= 0:
        answer = True
    return answer

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]
def union(a,b):
    a,b = find(a),find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n = int(input())
coordinate = [ list(map(int,input().split())) for _ in range(n)]
parents = [ i for i in range(n) ]

for i in range(n):
    for j in range(i+1,n):
        if check(coordinate[i],coordinate[j]) and find(i) != find(j):
            union(i,j)

for i in range(n):
    parents[i] = find(parents[i])
print(len(list(set(parents))))
print(parents.count(max(parents,key = parents.count)))