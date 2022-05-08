import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

pos = [0] * (n+1)
for i in range(n):
    pos[inorder[i]] = i

def f(in_start,in_end,p_start,p_end):

    if (in_start > in_end) or (p_start > p_end):
        return

    parents = postorder[p_end]
    print(parents,end=' ')

    left = pos[parents]-in_start
    right = in_end - pos[parents]

    f(in_start,in_start+left-1,p_start,p_start+left-1)
    f(in_end-right+1,in_end,p_end-right,p_end-1)

f(0,n-1,0,n-1)