N = int(input())

for i in range(N):
    str_Ns = str(i)
    sum = i
    for str_N in str_Ns:
        sum += int(str_N)

    if sum == N:
        print(i)
        break
    if i == N-1:
        print(0)