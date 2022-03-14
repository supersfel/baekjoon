n = int(input())
lst = [[0,0]] + [ list(map(int,input().split())) for _ in range(n) ]
nlst = [ 0,lst[1][0] ] + [ lst[i][1] for i in range(1,n+1)]
dp = [ [0 for _ in range(n+2)] for i in range(n+2)]

for i in range(3,n+2):
    for j in range(1,n+3-i):
        # print('i',i,'j',j)
        tmp =[]
        for k in range(i-2):
            tmp.append( dp[j][j+k+1] + dp[j+k+1][j+i-1] + nlst[j] * nlst[i+j-1] * nlst[j+k+1] )
        dp[j][j+i-1] = min(tmp)

    # for p in dp:
    #     print(p)
    # print('--------------')

print(dp[1][n+1])



