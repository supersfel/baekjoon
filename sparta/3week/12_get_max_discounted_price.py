shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons, discounted_price):
    # 이 곳을 채워보세요!
    prices.sort()
    price = prices.pop()
    coupon = coupons.pop()
    discounted_price += price * (100 - coupon) / 100

    if len(prices) < 1:
        return discounted_price
    if len(coupons) < 1:
        for a in prices:
            discounted_price += a

        return discounted_price


    return get_max_discounted_price(prices,coupons,discounted_price)




print(get_max_discounted_price(shop_prices, user_coupons,0))  # 926000 이 나와야 합니다.
