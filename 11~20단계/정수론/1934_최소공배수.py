n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    num = a*b

    while b > 0:
        a,b = b, a % b

    print(num // a)