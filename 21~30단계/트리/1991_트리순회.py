n = int(input())
tree = [ [0,0,0] for _ in range(n)]

for _ in range(n):
    node,left,right = map(str,input().split())
    idx = ord(node)-ord('A')
    tree[idx]= [node,left,right]

def pre(node):
    idx = ord(node)-ord('A')
    print(node,end='')
    if tree[idx][1] != ".":
        pre(tree[idx][1])
    if tree[ord(node)-ord('A')][2] != ".":
        pre(tree[idx][2])
def middle(node):
    idx = ord(node)-ord('A')

    if tree[idx][1] != ".":
        middle(tree[idx][1])
    print(node,end='')
    if tree[ord(node)-ord('A')][2] != ".":
        middle(tree[idx][2])
def post(node):
    idx = ord(node)-ord('A')
    if tree[idx][1] != ".":
        post(tree[idx][1])
    if tree[ord(node)-ord('A')][2] != ".":
        post(tree[idx][2])
    print(node, end='')



pre('A')
print()
middle('A')
print()
post('A')