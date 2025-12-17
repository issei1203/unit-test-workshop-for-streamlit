import pytest
from src.session3 import api

# ====================================================================
# 【重要】モック設定をカプセル化したフィクスチャ
# ====================================================================

@pytest.fixture
def success_mock_get(mocker):
    """
    HTTP 200 OK の応答を返すように requests.get を設定するフィクスチャ。
    """
    # 応答オブジェクトの振る舞いを設定
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Taro"}

    # requests.get を置き換え、そのモックオブジェクトを返す
    mock_get = mocker.patch('src.session3.api.requests.get', return_value=mock_response)

    # 戻り値としてモックオブジェクト自体を返す
    return mock_get

# ====================================================================
# 設定済みフィクスチャを使用したテスト
# ====================================================================

def test_get_data_success(success_mock_get):
    """
    success_mock_get (200 OK応答) を使って、成功ケースをテストする。
    """

    # 1. テスト対象の関数を実行
    result = api.get_data()

    # 2. 検証
    # 期待されるデータが返されたか
    assert result == True

def test_get_data_request_called_once(success_mock_get):
    """
    リクエスト先が正しいか検証する。
    """
    api.get_data() # 実行

    expected_url = "https://example.com/"

    success_mock_get.assert_called_once_with(expected_url)


def test_get_data_failure():
    """
    failure_mock_get (404 応答) を使って、失敗ケースをテストする。
    """

    pass

def test_get_data_with_header():
    """
    mockの設定してパラメータチェックのテストをする。
    """
    pass