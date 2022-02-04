string=input()
while(string != '.'):
    lst = []

    for i in string:
        if i =='(' or i =='[':
            lst.append(i)
        elif i==')':
            if '(' not in lst:
                lst.append(i)
                break
            elif lst[-1] !='(':
                break
            else:
                lst.pop()
        elif i==']':
            if '[' not in lst:
                lst.append(i)
                break
            elif lst[-1] != '[':
                break
            else:
                lst.pop()


    print('yes' if len(lst) == 0 else 'no')
    string = input()

