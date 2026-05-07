import pandas as pd

df = pd.read_csv(r"H:\python_workshop\New folder\data.csv")


print("==== ORIGINAL DATA ====") 
print(df)

#---------------------------------------------
# PRECISION EXTRACTION
#---------------------------------------------

subgrid = df.iloc[[0, 2, 4], [0, 1]]
print("\n==== SUB GRID ====")
print(subgrid)

# Quantity and price 
plc_data = df.loc[df["Component"]== "PLC", ["Quantity","Price"]]
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

# AUTOMATED SYSTEM UPDATE (NO LOOPS)

df["Status"] = df["Quantity"].apply(lambda x: "URGENT" if x < 5 else "OK")

print("\n==== UPDATE DATA ====")
print(df)


#----------------------------------------------------
# LOGICAL REFLECTION (COMMENTS ONLY)
# ---------------------------------------------------

# Engineers avoid loops (for/while) when handling large datasets because:
# 1. Loops are slow when processing thousands/millions of rows.
# 2. Pandas uses vectorized operations (process all data at once).
# 3. Vectorization is much faster and more efficient.
# 4. Real systems (IoT, hospitals, factories) need real-time speed.
# 5. Less code = fewer bugs and cleaner programs.
