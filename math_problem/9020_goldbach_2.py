from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    n = int(input())

    for i in range(2,n//2 + 1):
        f = True
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                f = False
                break

        if f:
            for j in range(2, int((n-i)**0.5)+1):
                if (n-i) % j == 0:
                    f = False
                    break
            if f:
                num = i
    print(num,n-num)


















