
'''lst =['=','-','dz','lj','nj']
a = input()
count = 0
for b in lst:
    count += a.count(b)

print(len(a)-count)'''
string = input()
lst =['c=','c-','dz=','d-','lj','nj','s=','z=']
for a in lst:
    if a in string:
        string = string.replace(a,' ')
print(len(string))