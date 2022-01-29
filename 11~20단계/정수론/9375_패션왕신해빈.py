t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for i in range(n):
        name,type = map(str,input().split())
        if dic.get(type):
            dic[type] +=1
        else:
            dic[type] = 2
    result = 1
    for key,value in dic.items():
        result *= value
    print(result - 1)





