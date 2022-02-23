a,b,c = map(int,input().split())

def f(a,b):
    print(a,b)
    if b ==1:
        return a%c

    num = f(a,b//2)


    if b%2 ==0:
        return num * num%c
    else:
        return num * num*a%c

print(f(a,b))