# Google Ads 關鍵字 Top 5 分析工具

🔥 **教學延伸閱讀：** 如何偷取競爭對手流量 👉 https://www.anergyacademy.com/blog/how-to-steal-competitor-traffic/

本專案是一個簡單的 Python 工具，用於分析 **Google Ads Keyword Planner** 匯出的關鍵字資料。

---

## 📊 它會做什麼？

- 讀取 Google Ads Keyword Planner 匯出的 CSV（UTF-16，Tab 分隔）
- 自動清洗文字資料並轉換成可運算數字
- 找出 **搜尋量最高的前 5 個關鍵字**
- 計算「頁首出價（低 / 高）」的中位數
- 比較「Top 5 關鍵字」與「全部關鍵字」差異
- 匯出整理好的 Top 5 關鍵字報表（CSV）

---

## 🔧 主要功能

- 支援 Google Keyword Planner 匯出格式（UTF-16 + Tab 分隔）
- 自動將欄位轉換成可運算數值
- 找出搜尋量 Top 5 關鍵字
- 計算中位數（Top5 vs 全部）
- 自動匯出結果至 CSV

---

## 📁 輸入資料條件

必須為 Google Keyword Planner 匯出的 CSV，包含以下欄位：

- `Keyword`
- `Avg. monthly searches`
- `YoY change`
- `Top of page bid (low range)`
- `Top of page bid (high range)`

---

## ⚠️ 注意事項

- 檔案格式需為 `.csv`
- 編碼必須為 **UTF-16**
- 分隔符請使用 **Tab (\t)**
- Google 通常會在最上方產生描述內容，因此程式會跳過前 2 行
