T = int(input())
def sosu(num):
    f = False
    for i in range(2,int((num**0.5))+1):
        if num%i ==0:
            f = True
            break
    return f
for _ in range(T):
    n = int(input())
    a = n//2
    b = a
    while (sosu(a) or sosu(b)) :
        a-=1
        b+=1
    print(a,b)