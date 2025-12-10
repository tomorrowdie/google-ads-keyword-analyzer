import pandas as pd
import numpy as np

# 文件路径 - 修改为你的 CSV 文件位置
file_path = "D:/data/Anker_Google_Ads_Keyword_Stats_2025-12-10.csv"

# 读取 CSV 文件
# 跳过前 2 行，文件编码为 UTF-16，分隔符为 Tab
df = pd.read_csv(file_path, skiprows=2, encoding="utf-16", sep="\t")

# 转换数值列为数字类型
df['Avg. monthly searches'] = pd.to_numeric(
    df['Avg. monthly searches'], errors='coerce'
)
df['Top of page bid (low range)'] = pd.to_numeric(
    df['Top of page bid (low range)'], errors='coerce'
)
df['Top of page bid (high range)'] = pd.to_numeric(
    df['Top of page bid (high range)'], errors='coerce'
)

# 清理 YoY change 列（去除百分号）
df['YoY change (num)'] = (
    df['YoY change'].astype(str).str.replace('%', '', regex=False)
)
df['YoY change (num)'] = pd.to_numeric(df['YoY change (num)'], errors='coerce')

# ============================================
# 提取 Top 5 关键词（按月搜索量排序）
# ============================================
top5 = df.sort_values('Avg. monthly searches', ascending=False).head(5)

top5_selected = top5[[
    'Keyword',
    'Avg. monthly searches',
    'YoY change',
    'Top of page bid (low range)',
    'Top of page bid (high range)'
]]

print("🏆 Top 5 Keywords by Avg Monthly Searches:")
print(top5_selected)
print("\n")

# ============================================
# 计算中位数
# ============================================
median_low_top5 = np.median(top5['Top of page bid (low range)'].dropna())
median_high_top5 = np.median(top5['Top of page bid (high range)'].dropna())

median_low_all = np.median(df['Top of page bid (low range)'].dropna())
median_high_all = np.median(df['Top of page bid (high range)'].dropna())

print("💰 Median Bids Analysis:")
print(f"Top 5 - Median Low:  ${median_low_top5:.2f}")
print(f"Top 5 - Median High: ${median_high_top5:.2f}")
print(f"All Data - Median Low:  ${median_low_all:.2f}")
print(f"All Data - Median High: ${median_high_all:.2f}")

# ============================================
# 可选：导出分析结果到新的 CSV 文件
# ============================================
output_path = "D:/data/Top5_Keywords_Analysis.csv"
top5_selected.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n✅ Top 5 关键词已导出到: {output_path}")
