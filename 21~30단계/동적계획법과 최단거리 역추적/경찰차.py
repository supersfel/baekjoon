import sys

# 거리 구하는 함수
def dist(a, b):
    if b == 0:
        return N - w_list[a][0] + N - w_list[a][1]
    elif a == 0:
        return w_list[b][0] - 1 + w_list[b][1] - 1
    return abs(w_list[a][0] - w_list[b][0]) + abs(w_list[a][1] - w_list[b][1])


# 초기화
N = int(sys.stdin.readline())  # 도로의개수
W = int(sys.stdin.readline())  # 사건의수
w_list = [0]  # 사건리스트
for _ in range(W):  # 사건저장
    w_list.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(W + 1)] for _ in range(W + 1)]  # dp[x][y]=경찰1이 마지막으로 x를 처리하고 경찰2가 마지막으로 y를 처리했을때의 최소이동거리
dp_trace = [[0 for _ in range(W + 1)] for _ in range(W + 1)]  # 해당위치에 어떤 경찰차가 도착햇는지 표시

for i in range(1, W + 1):  # 모든 사건에 한쪽경찰만 이동할때
    if i == 1:  # 첫사건
        dp[i][0] = w_list[1][0] - 1 + w_list[1][1] - 1  # 경찰1이 이동할때
        dp[0][i] = N - w_list[1][0] + N - w_list[1][1]  # 경찰2가 이동할때
    else:  # 모든 사건에 한쪽경찰만 이동할때
        dp[0][i] = dp[0][i - 1] + dist(i - 1, i)
        dp[i][0] = dp[i - 1][0] + dist(i - 1, i)
    dp_trace[i][0] = i - 1
    dp_trace[0][i] = i - 1



# DP를 이용해 모든 경우의수 구하기
for i in range(1, W + 1):
    for j in range(1, W + 1):
        # 같을때는 없으므로 지나감
        if i < j:  # j가 더클때 2
            if i - j == -1:  # ex) 1차이날때 3,4로가 가는방법 3,0 3,1 3,2에서 갈수잇음
                for k in range(j - 1):
                    if k == 0:  # 0에서 바로올때
                        dp[i][j] = dp[i][k] + dist(j, k)
                        dp_trace[i][j] = 0
                    else:  # 여러방향에서 올 수 있을때 최솟값 구하기
                        if dp[i][j] > dp[i][k] + dist(j, k):
                            dp[i][j] = dp[i][k] + dist(j, k)
                            dp_trace[i][j] = k
            else:  # 1차이가 날때가아니면 넘어올수 잇는경우가 하나에없다. 2,4로 가는방법 2,3
                dp[i][j] = dp[i][j - 1] + dist(j - 1, j)
                dp_trace[i][j] = j - 1  # 어디에서 도착했는지
        if i > j:  # i가 더크면
            if i - j == 1:  # ex) 1차이날때 3,4로가 가는방법 3,0 3,1 3,2에서 갈수잇음
                for k in range(0, i - 1):
                    if k == 0:
                        dp[i][j] = dp[k][j] + dist(k, i)
                        dp_trace[i][j] = 0
                    else:
                        if dp[i][j] > dp[k][j] + dist(k, i):
                            dp[i][j] = dp[k][j] + dist(k, i)
                            dp_trace[i][j] = k
            else:  # 1차 날때가아니면 넘어올수 잇는경우가 하나에없다. 2,4로 가는방법 2,3
                dp[i][j] = dp[i - 1][j] + dist(i - 1, i)
                dp_trace[i][j] = i - 1  # 어디에서 도착했는지

# 구한것중 W값에 도착했을때 최소값 구하기
min_value = 99999999999999
police1 = 0
police2 = 0
for i in range(W + 1):
    if i != W:
        if dp[W][i] < min_value:
            min_value = dp[W][i]
            # 가장작을때의 경찰 위치저장
            police1 = W
            police2 = i
        if dp[i][W] < min_value:
            min_value = dp[i][W]
            police1 = i
            police2 = W

print(min_value)
# print(police1)
# print(police2)

# 저장된 경찰위치를 통해 역으로 추적
trace = []
for i in dp_trace:
    print(i)
for i in range(W):
    print(police1,police2)
    if police2 > police1:
        police2 = dp_trace[police1][police2]
        trace.append(2)
    else:
        police1 = dp_trace[police1][police2]
        trace.append(1)

# 이동 경로 출력
for i in range(W - 1, -1, -1):
    print(trace[i])