T = int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    print(H*100 + N // H  if N%H == 0 else (N % H) * 100 + N // H + 1)
