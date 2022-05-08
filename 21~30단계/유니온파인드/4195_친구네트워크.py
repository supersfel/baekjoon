import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
t=int(input())
def find(user):
    if parents[user][0] == user:
        return user
    parents[user][0] = find(parents[user][0])
    return parents[user][0]
def union(a,b):

    a,b = find(a),find(b)

    if parents[a][1] > parents[b][1]:
        parents[a][1] += parents[b][1]
        parents[b] = parents[a]
    else:
        parents[b][1] += parents[a][1]
        parents[a]= parents[b]

for _ in range(t):
    F = int(input())
    parents = {}
    for __ in range(F):
        users = list(map(str,input().split()))

        for user in users:
            if user not in parents:
                parents[user]=[user,1]

        if find(users[0]) != find(users[1]):
            union(users[0],users[1])
        print(parents[find(users[0])][1])
        #print(parents)

