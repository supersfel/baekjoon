from fractions import Fraction
n = int(input())
lst = list(map(int,input().split()))

first = lst[0]
for i in range(1,n):
    num=Fraction(first,lst[i])
    print(num.numerator,'/',num.denominator,sep='')
