import sys

input = sys.stdin.readline

N, K = map(int,input().split())

def factorial(N):
    fact = 1
    if N > 0:
        fact = N * factorial(N-1)
    return fact

def factorial_K(N,K):
    fact = 1
    if N > 0:
        fact = (N - K) * factorial(N - K -1)
    return fact

fact_N = factorial(N)
fact_M = factorial(K)
fact_N_K = factorial_K(N,K)

result = fact_N // (fact_M * fact_N_K)

result_str =  str(result)
reverse_str = result_str[::-1]


count = 0

for i in reverse_str:
    if i == '0':
        count += 1
    elif i != '0':
        break
print(count)