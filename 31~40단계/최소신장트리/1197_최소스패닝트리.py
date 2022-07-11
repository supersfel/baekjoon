import sys
input = sys.stdin.readline

def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]
#dd
def union(a,b):
    a,b = find(a),find(b)
    if a> b:
        parents[a] = b
    else:
        parents[b] = a

v,e = map(int,input().split())
parents = [ i for i in range(v+1)]
way = []
for i in range(e):
    a,b,c = map(int,input().split())
    way.append((a,b,c))

way.sort(key=lambda x : x[2])
result = 0
for a,b,c in way:
    if find(a) != find(b):
        union(a,b)
        result += c
print(result)


