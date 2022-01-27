t = int(input())
fac =[1]
for i in range(1,31):
    fac.append(fac[-1] * i)

for _ in range(t):
    n,m = map(int,input().split())
    print( fac[m] // (fac[n] * fac[m-n]) )

