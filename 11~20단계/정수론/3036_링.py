from fractions import Fraction
n = int(input())
lst = list(map(int,input().split()))

first = lst[0]
for i in range(1,n):
    num=Fraction(first,lst[i])
    print(num.numerator,'/',num.denominator,sep='')


# a = int(input())
# ring = list(map(int, input().split()))
# for i in ring:
#     if i != ring[0]:
#         a, b = ring[0],i
#         a_c,b_c = a,b
#         while True:
#             a, b = b, a%b
#             if b==0:
#                 break
#         print('%d/%d'%(int(a_c/a),int(b_c/a)))