T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    lst =[[j for j in range(1,15)]]

    for i in range(k):
        f_lst = [1]
        p=1
        for j in range(1,14):
            p += lst[i][j]
            f_lst.append(p)
        lst.append(f_lst)

    print(lst[k][n-1])

    # 1  4  10 20 35 56 84
    # 1  3  6  10 15 21 28
    # 1  2  3  4  5  6  7

