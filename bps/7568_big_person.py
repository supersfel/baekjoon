rank_lst,lst =[],[[100,100],[100,100],[100,100],[100,100],[99,101],[100,101]]

# rank_lst,lst =[],[]
cnt,rank=1,1
# N = int(input())
# for _ in range(N):
#     lst.append(list(map(int,input().split())))

def f(lst):
    global cnt,rank
    new_lst = []
    for i in lst:
        flag = 1
        for j in lst:
            if lst.index(i)==lst.index(j):
                continue
            if i[0]<=j[0] and i[1]<=j[1]:
                flag =0
        if flag:
            rank_lst.append(i + [rank])
            cnt +=1
        else:
            new_lst.append(i)
    rank =cnt

    if len(new_lst) >0:
        f(new_lst)
    return rank_lst

f(lst)

for i in lst:
    for j in rank_lst:
        if i[0]==j[0] and i[1]==j[1]:
            print(j[2],end=' ')
            break
