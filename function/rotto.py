import random
def lotto():
    number = random.randint(1, 46)
    return number

lst=[]
while len(lst)!=6:
    num = lotto()
    if num not in lst:
        lst.append(num)

for i in lst:
    print(i)

