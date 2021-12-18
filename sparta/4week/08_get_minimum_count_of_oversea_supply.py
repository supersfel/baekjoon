import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    heap = []
    need_stock = k - stock
    count = 0

    for suppliy in supplies:
        heapq.heappush(heap,suppliy * -1)

    sum_need_stock = 0
    while sum_need_stock < need_stock:
        sum_need_stock += heapq.heappop(heap) * -1
        count +=1

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))