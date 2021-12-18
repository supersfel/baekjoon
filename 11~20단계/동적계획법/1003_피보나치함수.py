zero = [1, 0, 1]
one = [0, 1, 1]
def fibo(num):
    if num >= len(zero):
        for i in range(len(zero), num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num],one[num])


T = int(input())

for _ in range(T):
    fibo(int(input()))