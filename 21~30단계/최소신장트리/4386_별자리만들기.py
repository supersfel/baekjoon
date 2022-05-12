import sys
input = sys.stdin.readline

n = int(input())
star=[]
for _ in range(n):
    x,y = map(float,input().split())
    star.append((x,y))

distance=[]
for i in range(n):
    for j in range(i,n):
        if i == j:
            continue
        dist = (( star[i][1] - star[j][1] )**2 + ( star[i][0]-star[j][0])**2)**0.5
        distance.append((i+1,j+1,dist))


parents=[i for i in range(n+1)]
def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a,b = find(a),find(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a

distance.sort(key=lambda x : x[2])
result = 0
for a,b,c in distance:
    if find(a) != find(b):
        union(a,b)
        result += c
print(round(result,2))