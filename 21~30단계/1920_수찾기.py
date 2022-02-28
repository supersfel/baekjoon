import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
find_lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

def f(num, start, end):
    global result
    middle = start + (end - start) // 2
    if num == lst[middle]:
        result = 1
        return
    if (end-start)==1:
        if num==lst[start] or num == lst[end]:
            result=1
        return

    if num > lst[middle]:
        f(num, middle, end)
    else:
        f(num, start, middle)

for i in find_lst:
    result = 0
    f(i,0,n-1)
    print(result)




