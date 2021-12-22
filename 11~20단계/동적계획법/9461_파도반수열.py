lst = [1,1,1]
for i in range(3,100):
    lst.append(lst[i-2]+lst[i-3])

T = int(input())
for _ in range(T):
    print(lst[int(input())-1])

