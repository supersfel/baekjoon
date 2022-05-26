a,b,v = map(int,input().split())

cnt = 0
height = 0
while(1):
    cnt +=1
    height += a
    if height >= v:
        break
    height -= b
print(cnt)