import pandas as pd
import numpy as np

df = pd.read_csv(r"H:\python_workshop\New folder\data.csv")

print("==== ORIGINAL DATA ====")
print(df)

# ─────────────────────────────────────────────
# YOUR DAY 5 CODE (kept exactly as-is)
# ─────────────────────────────────────────────

subgrid = df.iloc[[0, 2, 4], [0, 1]]
print("\n==== SUB GRID ====")
print(subgrid)

plc_data = df.loc[df["Component"] == "PLC", ["Quantity", "Price"]]
print("\n==== PLC DATA =====")
print(plc_data)

high_risk = df[(df["Price"] > 800) & (df["Quantity"] < 10)]
print("\n==== HIGH RISK ITEMS ====")
print(high_risk)

filtered = df[(df["Category"] == "Electrical") | (df["Price"] < 100)]
print(filtered)

test = df[df["Price"] > 5000]
print("\n==== EMPTY CHECK ====")
if test.empty:
    print("No matching records found.")
else:
    print(test)

df["Status"] = df["Quantity"].apply(lambda x: "URGENT" if x < 5 else "OK")
print("\n==== UPDATE DATA ====")
print(df)

# ─────────────────────────────────────────────
# DAY 6 STARTS HERE
# ─────────────────────────────────────────────

# Introduce some NaN values to simulate dirty data
df.loc[0, "Price"] = np.nan
df.loc[2, "Quantity"] = np.nan
df.loc[4, "Category"] = np.nan

# GAP ANALYSIS 
print("\n==== MISSING VALUE REPORT ====")
print(df.isnull().sum())

# Number columns → fill with Mean
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())


df["Category"] = df["Category"].fillna("Unknown")

print("\n==== AFTER CLEANING ====")
print(df)
print("Missing values left:", df.isnull().sum().sum())


print("\n==== CATEGORY SUMMARY ====")
category_summary = df.groupby("Category").agg(
    Total_Price  = ("Price",    "sum"),
    Avg_Quantity = ("Quantity", "mean")
).round(2)
print(category_summary)

# Group by Category → Max Price → only show where Avg Quantity > 5
print("\n==== MAX PRICE WHERE AVG QUANTITY > 5 ====")
result = (
    df.groupby("Category")
    .agg(Max_Price=("Price", "max"), Avg_Quantity=("Quantity", "mean"))
    .query("Avg_Quantity > 5")
    .round(2)
)
print(result)


df.to_csv(r"H:\python_workshop\New folder\refined_data_YourName.csv", index=False)
print("\n==== FILE SAVED: refined_data_YourName.csv ====")