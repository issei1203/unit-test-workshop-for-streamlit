from src.session1 import discounter

# ====================================================================
# テストケースの基本方針：
# 分岐処理（price > 1000）を網羅するために、
# 「1000円より大きい場合」「1000円より小さい場合」「境界値（1000円）の場合」
# の3パターンを検証する。
# ====================================================================

# テストケース1: 割引が適用される場合 (価格 > 1000)
def test_discount_applied():
    # 1001円は割引対象となる
    price = 1001
    expected_price = 900  # 1001 * 0.9 = 900.9 -> int(900.9) = 900

    result = discounter.calculate_discount(price)

    assert result == expected_price

# テストケース2: 割引が適用されない場合 (価格 <= 1000)
def test_no_discount_applied_below_threshold():
    # 500円は割引対象外となる
    pass

# テストケース3: 境界値のテスト (価格 == 1000)
def test_boundary_value_at_threshold():
    # 1000円も割引対象外となる (条件が price > 1000 のため)
    pass
