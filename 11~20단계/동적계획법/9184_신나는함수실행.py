# from itertools import product
# def w(a,b,c):
#     if a<=0 or b<=0 or c<=0:
#         return 1
#     elif a>20 or b > 20 or c > 20:
#         return w(20,20,20)
#     elif b>=a or c >=a: #추가한 부분
#         return 2**a
#     else:
#         return w(a-1,b,c) +w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
#
#
# lst= [1,2,3,4,5,6,7,8,9,10]
# for i in product(lst,repeat=3):
#     print(i,end=' : ')
#     num = w(i[0],i[1],i[2])
#     print(num)
#
# print(w(-1,-1,-1))

lst = [[[1]*3]*3]*3
print(lst)
for i in lst:
    for j in i:
        print(j)
    print('------------')


lst[1][1][1] = 3
print('change')

print('------------')
for i in lst:
    for j in i:
        print(j)
    print('------------')

print('무식하게 찍어보기')
print('------------')

print(lst[0][0][0],lst[0][0][1],lst[0][0][2])
print(lst[0][1][0],lst[0][1][1],lst[0][1][2])
print(lst[0][2][0],lst[0][2][1],lst[0][2][2])
print('')
print(lst[0][0][0],lst[1][0][1],lst[2][0][2])
print(lst[0][1][0],lst[1][1][1],lst[2][1][2])
print(lst[0][2][0],lst[1][2][1],lst[2][2][2])
print('')
print(lst[0][0][0],lst[1][0][1],lst[2][0][2])
print(lst[0][1][0],lst[1][1][1],lst[2][1][2])
print(lst[0][2][0],lst[1][2][1],lst[2][2][2])



