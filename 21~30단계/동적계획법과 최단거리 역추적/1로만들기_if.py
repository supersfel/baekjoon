# 1463
N = int(input())
cnt = 0

while(N != 1):
    if (N-1) % 3 == 0:
        N = (N-1) //3
        cnt += 2
    if N % 3 == 0:
        N //= 3
    if N % 2 == 0:
        N //= 2
    else:
        if (N-2) % 3 == 0:
            cnt += 2
            N -= 2
            continue
        else:
            N -= 1
    cnt += 1

print(cnt)