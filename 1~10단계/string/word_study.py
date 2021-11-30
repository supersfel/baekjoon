a = input().upper()
u_a = list(set(a))



for x in u_a:
    cnt = a.count(x)
    b.append(cnt)


if b.count(max(b)) > 1 :
    print('?')
else :
    #print(max(a,key = a.count))   #왜 시간초과가 뜰까여
    print(u_a[b.index(max(b))])