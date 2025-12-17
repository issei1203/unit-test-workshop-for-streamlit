# test_sample_errors.py (手本として提示するコード)

import pytest
from src.session2 import error_raiser

# ====================================================================
# 例外が発生することを確認するためのテスト（手本 - TypeError検証）
# ====================================================================

def test_trigger_error_raises_type_error():
    """
    負の値を入力した際に、TypeError が発生することを検証する。
    """
    # pytest.raises() に「TypeError」を指定
    with pytest.raises(TypeError):
        # このブロック内のコードを実行すると、TypeError が発生することが期待される
        error_raiser.raise_error(-10)