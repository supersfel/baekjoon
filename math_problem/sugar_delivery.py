N = int(input())
bong = 0

for i in range(N//5+1):
    if (N-(i*5))%3 == 0:
        bong = i

print(bong + (N-bong*5)//3 if (N-bong*5)%3 == 0 else -1)


