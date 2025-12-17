def raise_error(input_value):
    """
    入力値が負の場合に TypeError を発生させる関数 (テストの手本用)
    """
    if input_value < 0:
        # TypeError を発生させる
        raise TypeError("負の値は型が不適切です")
    return input_value