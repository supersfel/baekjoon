import sys
sys.setrecursionlimit(10**5)
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start,end):

    if start>end:
        return
    div = end + 1

    for i in range(start,end+1):
        if preorder[start] < preorder[i]:
            div=i
            break

    postorder(start+1,div-1)
    postorder(div,end)
    print(preorder[start])

postorder(0,len(preorder)-1)