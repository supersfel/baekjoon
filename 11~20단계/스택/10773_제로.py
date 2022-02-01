import sys
k = int(sys.stdin.readline())
lst=[]
for _ in range(k):
    num = int(sys.stdin.readline())
    if num !=0:
        lst.append(num)
    else:
        lst.pop()

print(sum(lst))