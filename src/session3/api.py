import requests

def get_data():
    """
    外部APIを呼び出してユーザー情報を取得する関数。
    """
    response = requests.get(f"https://example.com/")

    if response.status_code == 200:
        return True
    else:
        return False

def get_data_with_header():
    response = requests.get(f"https://example.com/", headers={"sample": "sample"})

    if response.status_code == 200:
        return True
    else:
        return False