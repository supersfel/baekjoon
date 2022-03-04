h,m = map(int,input().split())
time = int(input())

m += time
h += m//60
m = m%60
h = h%24

print(h,m)