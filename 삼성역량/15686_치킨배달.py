import sys
input = sys.stdin.readline

n,m = map(int,input().split())
city = [ list(map(int,input().split())) for _ in range(n)]

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickens.append([i,j])
        elif city[i][j] == 1:
            houses.append([i,j])

def get_dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return abs(x1-x2) + abs(y1-y2)

def get_chicken_dist():
    chicken_dist = 0

    for house in houses:
        dist = 1e9
        for i in range(len(chickens)):
            if visited[i]:
                dist = min(dist,get_dist(house,chickens[i]))
        chicken_dist += dist
    return chicken_dist

visited = [0]*len(chickens)
result = 1e9
def dfs(idx,cnt):
    global result
    if cnt == m:
        result = min(result,get_chicken_dist())
        return

    for i in range(idx,len(chickens)):
        if not visited[i] :
            visited[i] = 1
            dfs(idx+1,cnt+1)
            visited[i] = 0


dfs(0,0)
print(result)