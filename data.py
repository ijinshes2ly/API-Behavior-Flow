```python
import pandas as pd

# 하드코딩된 사용자 행동 흐름 데이터 (30일)
data = {
    "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "Landing_Page": [
        "Homepage", "Product Page", "Blog", "Pricing", "Contact"] * 6,
    "Exit_Page": [
        "Product Page", "Homepage", "Pricing", "Blog", "Contact"] * 6,
    "Bounce_Rate": [
        45.2, 50.1, 55.3, 40.8, 48.5,
        46.0, 49.5, 54.2, 39.9, 47.8,
        44.8, 51.2, 53.1, 41.5, 49.0,
        45.9, 48.7, 52.0, 40.2, 48.2,
        44.5, 50.6, 51.5, 39.5, 47.5,
        46.2, 49.3, 50.8, 38.9, 46.8
    ],
    "Average_Session_Duration": [
        180, 240, 150, 300, 200,
        190, 250, 140, 310, 210,
        185, 245, 160, 290, 205,
        175, 255, 155, 320, 195,
        180, 260, 165, 295, 185,
        170, 270, 170, 280, 190
    ]
}

# 데이터프레임 생성 및 CSV 저장
csv_filename = "user_behavior_data.csv"
user_behavior_data = pd.DataFrame(data)
user_behavior_data.to_csv(csv_filename, index=False)

print(f"CSV 파일 '{csv_filename}' 저장 완료!")
```
