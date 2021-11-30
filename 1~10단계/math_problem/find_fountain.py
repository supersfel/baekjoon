t = int(input())
a=0
f=1
while (a*(a+1)/2 < t):
    a+=1
b=a
for c in range(t-(a-1)*a//2-1):
    f += 1
    b -= 1

if (a%2 ==0):
    print(f, '/', b, sep ="")
else :
    print(b, '/', f, sep="")



