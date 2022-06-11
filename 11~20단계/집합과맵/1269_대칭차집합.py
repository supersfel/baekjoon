import sys
input = sys.stdin.readline
a,b = map(int,input().split())
A_lst = set(map(int,input().split()))
B_lst = set(map(int,input().split()))

result = print( len((A_lst - B_lst) | (B_lst-A_lst)) )