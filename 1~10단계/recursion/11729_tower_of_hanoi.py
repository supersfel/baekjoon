lst=[]
def f(start,end,N):
    if N==1:
        lst.append([start,end])
    else:
        f(start,6-start-end,N-1)
        lst.append([start,end])
        f(6-start-end,end,N-1)

f(1,3,int(input()))
print(len(lst))
for i in lst:
    print(i[0],i[1])