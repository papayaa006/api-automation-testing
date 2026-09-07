import pytest
import requests

BASE_URL = "https://reqres.in/api"


# 驗證成功取得單一使用者資料

def test_get_user_success():
    user_id = 2
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    assert response.status_code == 200

    assert response.elapsed.total_seconds() < 2.0

    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == user_id
    assert data["data"]["email"] == "janet.weaver@reqres.in"

# 驗證查詢不存在的使用者時，系統是否正確回應 404
def test_get_user_not_found():
    invalid_id = 99999
    response = requests.get(f"{BASE_URL}/users/{invalid_id}")

    assert response.status_code == 404

    assert response.json() == {}


# 使用 pytest.mark.parametrize 一次驗證多組輸入與預期結果

@pytest.mark.parametrize(
    "name, job",
    [
        ("Alice", "QA Engineer"),
        ("Bob", "Backend Developer"),
        ("Charlie", "Product Manager"),
    ],
)
def test_create_user(name, job):
    payload = {"name": name, "job": job}

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == name
    assert data["job"] == job

    assert "id" in data
    assert "createdAt" in data