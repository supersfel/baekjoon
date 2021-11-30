a,b,c = map(int,input().split())
print((c-a)//(a-b) + 1 if ((c-a)%(a-b)==0) else (c-a)//(a-b))
