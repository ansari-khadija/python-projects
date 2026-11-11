
# ==========================================
# XGBOOST - BUSINESS PROFIT & LOSS
# ==========================================

import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Create sample dataset
sales = {
    "Year": [
        2012, 2013, 2014, 2015, 2016,
        2017, 2018, 2019, 2020, 2021,
        2022, 2023, 2024, 2025, 2026
    ],

    "Shoes_Sold": [
        150, 200, 580, 250, 720,
        300, 1100, 400, 180, 550,
        850, 350, 1500, 500, 2100
    ],

    "Revenue": [
        75000, 100000, 290000, 125000, 360000,
        150000, 550000, 200000, 90000, 275000,
        425000, 175000, 750000, 250000, 1050000
    ],

    "Expenses": [
        150000, 180000, 250000, 200000, 300000,
        220000, 420000, 280000, 190000, 320000,
        390000, 250000, 580000, 350000, 750000
    ],

    "Marketing_Cost": [
        15000, 18000, 22000, 25000, 30000,
        35000, 45000, 50000, 20000, 25000,
        40000, 55000, 65000, 80000, 95000
    ],

    "Returned_Shoes": [
        45, 50, 35, 60, 45,
        70, 55, 85, 100, 85,
        65, 90, 55, 110, 45
    ]
}

df = pd.DataFrame(sales)

# Calculate profit/loss
df["Profit_Loss"] = df["Revenue"] - df["Expenses"]

# Identify status
df["Status"] = np.where(
    df["Profit_Loss"] >= 0,
    "Profit",
    "Loss"
)

print(df)

# Count profit and loss years
print("\nBusiness Summary:")
print(df["Status"].value_counts())

# 2. Create Profit/Loss target

df["Profit_Loss"] = np.where(
    df["Revenue"] > df["Expenses"], 1, 0
)

# 1 = Profit
# 0 = Loss

# 3. Select features and target

X = df[["Year", "Shoes_Sold", "Revenue", "Expenses"]]
y = df["Profit_Loss"]

# 4. Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# 5. Create XGBoost classifier

model = xgb.XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    eval_metric="logloss",
    random_state=42
)

# 6. Train model

model.fit(X_train, y_train)

# 7. Make predictions

predictions = model.predict(X_test)

# 8. Evaluate model

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# 9. Feature importance

print("Feature Importance:")
print(model.feature_importances_)

# 10. Scatter Plot - Profit vs Loss

profit_data = df[df["Profit_Loss"] == 1]
loss_data = df[df["Profit_Loss"] == 0]

plt.figure(figsize=(10, 5))

# Profit points and line
plt.plot(
    profit_data["Year"],
    profit_data["Revenue"] - profit_data["Expenses"],
    color="#29802D",
    marker="o",
    linestyle="-",
    label="Profit"
)

# Loss points and line
plt.plot(
    loss_data["Year"],
    loss_data["Revenue"] - loss_data["Expenses"],
    color="#2D4594",
    marker="o",
    linestyle="-",
    label="Loss"
)

plt.axhline(0, color="black", linewidth=1)

plt.title("Business Profit vs Loss")
plt.xlabel("Year")
plt.ylabel("Profit / Loss Amount")

plt.legend()
plt.grid(True, alpha=0.3)
plt.show()