def append_star(len):
    if len == 1:
        return ['*']

    Stars = append_star(len//3)
    lst = []

    for s in Stars:
        lst.append(s *3)
    for s in Stars:
        lst.append(s + ' '*(len//3) + s)
    for s in Stars:
        lst.append(s *3)


    return lst

n=int(input())
print('\n'.join(append_star(n)))