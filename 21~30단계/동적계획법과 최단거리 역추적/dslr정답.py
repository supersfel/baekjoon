
def f1(num):
    D = (2 * num) % 10000

    S = (num - 1) % 10000

    L = (10 * num + (num // 1000)) % 10000

    R = (num // 10 + (num % 10) * 1000) % 10000

    return [D,S,L,R]

def f2(num):
    d1, d2, d3, d4 = num
    D = str(2 * int(num) % 10000)
    D = '0' * (4 - len(D)) + D

    if int(num) == 0:
        S = '9999'
    else:
        S = str(int(num) - 1)
        S = '0' * (4 - len(S)) + S
    L = d2 + d3 + d4 + d1
    R = d4 + d1 + d2 + d3
    return [int(D),int(S),int(L),int(R)]

for i in range(10000):
    a = f1(i)

    i = '0' * (4 - len(str(i))) + str(i)
    b = f2(i)

    if a!= b:
        print('---------------------')
        print(i)
        print(a)
        print(b)