N = int(input())

lst =[0]*N
count=0

def f(queen,col):
    global count
    if col==N:
        count +=1
        return

    for i in range(N):
        queen[col] = i

        for x in range(col):
            if queen[x] == queen[col]:
                break
            if abs(queen[x]-queen[col]) == (col-x):
                break
        else:
            f(queen,col+1)

f(lst,0)
print(count)

#파이썬으로는 푸는거 불가
#answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
#print(answer[int(input())])