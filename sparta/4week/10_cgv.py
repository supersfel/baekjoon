seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 1
}
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    non_vip_lst = []
    non_vip_small_lst = []
    count = 1

    for person in range(1,total_count + 1):

        if person not in fixed_seat_array:
            non_vip_small_lst.append(person)
        else :
            non_vip_lst.append(non_vip_small_lst)
            non_vip_small_lst = []

    non_vip_lst.append(non_vip_small_lst)

    for non_vip_people in non_vip_lst:

        count *= fibo_dynamic_programming(len(non_vip_people)+1,memo)





    return count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))