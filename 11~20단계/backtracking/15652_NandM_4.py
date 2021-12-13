N,M = map(int,input().split())

lst = []

def f():
    if len(lst)==M:
        print(' '.join(map(str,lst)))
        return

    for i in range(1,N+1):
        if len(lst)==0 or i>=max(lst):
            lst.append(i)
            f()
            lst.pop()

f()