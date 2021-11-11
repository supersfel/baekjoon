T= int(input())

num = list(map(int,input().split()))
count=0
lst=[n for n in range(2,1000)]
for i in range(2,1000):
    for j in range(2,1000//i+1):
        if j*i in lst:
            lst.remove(j*i)
for n in num:
    if n in lst:
        count +=1
print(count)




