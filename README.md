![Tests](https://github.com/<你的GitHub帳號>/<你的Repo名稱>/actions/workflows/test.yml/badge.svg)
# RESTful API Automation Test Suite

基於 **Python + pytest + requests** 建構的自動化 API 測試腳本，針對公開 RESTful API（ReqRes）進行介面功能驗證、異常狀態攔截與多筆測資的資料驅動測試。

---

## 📌 專案特色

- **端到端 API 驗證**：驗證 HTTP 狀態碼（Status Code）、回應時間（Response Time）與 JSON 資料結構。
- **資料驅動測試 (Data-Driven Testing)**：利用 `@pytest.mark.parametrize` 批量注入多組測試資料，提高邊界與功能覆蓋率。
- **負面情境測試 (Negative Testing)**：驗證查無資源時系統是否正確回傳 404 與預期錯誤格式，確保容錯機制。

---

## 🛠 技術堆疊

- **開發語言**：Python 3.10+
- **測試框架**：`pytest`
- **HTTP 請求庫**：`requests`

---

## 🧪 測試案例涵蓋範圍 (Test Cases)

| 測試案例函式 | 測試類型 | 驗證重點 |
| :--- | :--- | :--- |
| `test_get_user_success` | 正向測試 (Happy Path) | 驗證查詢單一使用者：HTTP 200、回應時間 < 2.0s、關鍵欄位（ID、Email）符合預期 |
| `test_get_user_not_found` | 負向測試 (Negative Test) | 驗證查詢不存在的 ID（99999）：系統正確回應 HTTP 404 與空回應 |
| `test_create_user` | 參數化測試 (DDT) | 批量驗證多組不同姓名與職稱建立：HTTP 201 Created、伺服器回傳 ID 與建立時間 |

---

## 🚀 快速開始 (Getting Started)

### 1. 安裝相依套件

確認本機具備 Python 環境後，安裝必要套件：

```bash
pip install requests pytest
