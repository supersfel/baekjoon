x,y,d,t = map(int,input().split())
dist =( x*x + y *y ) **0.5

if t > d:
    print(dist)
else:
    n = dist // d
    if d < dist:
        print(min(t*n+dist-d*n,t*(n+1)))
    else:
        print(min(dist,t+d-dist,2*t))