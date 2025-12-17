def calculate_discount(price):
    """
    価格に基づいて割引後の価格を計算する。

    - 価格が1000円以下の場合は割引なし。
    - 価格が1000円を超える場合は10%割引を適用。
    """
    if price > 1000:
        # 分岐1: 1000円より高い場合 (10%割引)
        discounted_price = price * 0.9
        return int(discounted_price)
    else:
        # 分岐2: 1000円以下の場合 (割引なし)
        return price