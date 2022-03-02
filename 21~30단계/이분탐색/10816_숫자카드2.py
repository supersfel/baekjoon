import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
find_lst = list(map(int,sys.stdin.readline().split()))

count ={}
for i in lst:
    try : count[i] +=1
    except : count[i]=1

for i in find_lst:
    try : print(count[i],end= ' ')
    except : print('0',end= '  ')
