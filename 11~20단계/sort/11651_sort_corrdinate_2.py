import sys
N = int(sys.stdin.readline())
lst=[]
for _ in range(N):
    a,b = list(map(int,sys.stdin.readline().split()))
    lst.append([b,a])

lst.sort()

for i in lst:
    print(i[1],i[0])

# import sys
# N = int(sys.stdin.readline())
# lst=[]
# for _ in range(N):
#     a,b = list(map(int,sys.stdin.readline().split()))
#     lst.append([a,b])
#
# lst.sort(key = lambda x : x[1])
#
# for i in lst:
#     print(i[0],i[1])