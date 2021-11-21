def f(lst,N):
    if N==1:  #탈출 조건
        for _ in range(len(lst)):
            for k in range(len(lst[_])):
                print(lst[_][k], end='')
            print('')
        return

    new_lst=[[]]*(3*len(lst))
    l = len(lst)
    for i in range(len(new_lst)):
        if 2 * l > i >= l:
            new_lst[i] = lst[i%l]+[' ']* l+lst[i%l]
        else :
            new_lst[i] = lst[i % l] + lst[i % l] + lst[i % l]

    return f(new_lst,N-1)

first_lst =[['*','*','*'],['*',' ','*'],['*','*','*']]
N = int(int(input())**(1/3))
f(first_lst,N)

#메모리 초과

# 111
# 101
# 111
#
# 111111111
# 101101101
# 111111111
# 111000111
# 101000101
# 111000111
# 111111111
# 101101101
# 111111111