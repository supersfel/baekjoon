n,m = map(int,input().split())
five = [ 5**x for x in range(1,14)]
two =  [ 2**x for x in range(1,31)]

def get_five(num):
    count = 0
    for i in five:
        count += num // i
    return count

def get_two(num) :
    count = 0
    for i in two:
        count += num // i
    return count



print( min( get_five(n) - get_five(m) - get_five(n-m)  , get_two(n) - get_two(m) - get_two(n-m) )  )


