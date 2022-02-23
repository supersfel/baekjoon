import sys
n,k = map(int,sys.stdin.readline().split())
num = 1000000007

def f(a,b):
    if b ==1:
        return a%num
    d = f(a,b//2)
    if b%2 ==0:
        return d * d%num
    else:
        return d * d*a%num



fac = [ 1 for _ in range(n+1)]

for i in range(2,n+1):
    fac[i] = fac[i-1] * i % num



a = fac[n]
b = fac[n-k] * fac[k] % num

print((a % num) * (f(b,num-2) % num)%num)