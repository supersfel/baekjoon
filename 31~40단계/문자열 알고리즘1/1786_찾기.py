t = input()
p = input()

k=[0 for _ in range(len(p))]
j=0
for i in range(1,len(p)):
    while j>0 and p[i]!=p[j]: # j랑 일치하지 않을때
        j = k[j-1] #가장 최근에 맞았던 부분으로 이동
    if p[i] == p[j]: #일치하면
        j+=1 #j값에 1 더해줌
        k[i]=j #k값 업데이트

result=[]
j=0
for i in range(len(t)):
    while j>0 and t[i]!=p[j]:
        j = k[j-1]
    if t[i]==p[j]:
        if j == len(p)-1:
            result.append(i-len(p)+2)
            j=k[j]
        else:
            j+=1

print(len(result))
print(*result)



