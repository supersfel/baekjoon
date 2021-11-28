MAP = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

N,M = map(int,input().split())
input_map=[[]]*N
for i in range(N):
    input_map[i]=input()

def count_map(map):
    count =0
    for m in range(len(map)):
        for n in range(len(map[m])):
            if map[m][n] != MAP[m][n]:
                count +=1
    return min(count,64-count)

result = 9999
for i in range(N-7):
    for j in range(M-7):

        new_map = [[]] * 8
        for k in range(i,i+8):
            new_map[k-i] = input_map[k][j:j+8]

        num =count_map(new_map)
        if num < result:
            result = num

print(result)