#소수를 찾는 문제
input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    lst = []
    for a in list(range(2,number+1)):
        for b in list(range(a+1,number+1)):
            if (b%a == 0):
                lst.append(b)

    lst = list(set(lst))

    full_lst = list(range(1,number+1))

    sosu_lst = [x for x in full_lst if x not in lst]

    return sosu_lst



result = find_prime_list_under_number(input)
print(result)

