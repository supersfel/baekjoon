a = input()

lst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
count = 0

for b in a:

    for c in lst:
        if b in c:
            count += lst.index(c) + 3


print(count)