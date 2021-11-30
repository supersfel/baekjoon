def factorial(N):
    if N in (0,1):
        return 1
    return N * factorial(N-1)

print(factorial(int(input())))

# a = int(input())
# result = 1
#
# for i in range(a):
#   while a !=0:
#     result *= a
#     a -= 1
#
# print(result)