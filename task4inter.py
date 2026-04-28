import pandas as pd


# THE SINGLE DIMENSION (Series)

components = ["Motor", "Sensor", "PLC", "Actuator", "Valve"]
prices = [120.5, 350.0, 500.75, 80.25, 210.0]

series_data = pd.Series(prices, index=components)

print("=== Pandas Series ===")
print(series_data)

print("\nPrice of Motor:", series_data["Motor"])


#THE DATA BLUEPRINT (DataFrame)

data = {
    "Component_Name": ["Sensor", "Motor", "PLC", "Valve", "Actuator"],
    "Quantity": [15, 8, 20, 12,5],
    "Unit_Price": [120.5, 350.0, 500.75, 80.25, 210.0]
}

df = pd.DataFrame(data)

print("\n=== DataFrame ===")
print(df)

print("\nShape of DataFrame:", df.shape)
print("Columns:", df.columns)

df["Total_Value"] = df["Quantity"] * df["Unit_Price"]

print("\n=== With Total Value ===")
print(df)

# One line: Display component names where Quantity > 10
print("\nComponents with Quantity > 10:")
print(df[df["Quantity"] > 10]["Component_Name"])
