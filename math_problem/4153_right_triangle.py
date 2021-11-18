lst=sorted(list(map(int,input().split())))
while(lst.count(0)!=3):
    print('right' if(lst[2] == (lst[0]**2 + lst[1]**2)**0.5)else 'wrong')
    lst = sorted(list(map(int, input().split())))
