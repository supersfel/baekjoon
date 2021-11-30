N = int(input())
lst=[]

for _ in range(N):
    lst.append(int(input()))

for a in sorted(lst):
    print(a)