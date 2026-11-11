
# ==========================================
# CATBOOST - SHOE BUSINESS PROFIT & LOSS
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from catboost import CatBoostClassifier, CatBoostRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import mean_absolute_error, r2_score

# ==========================================
# 1. CREATE SAMPLE DATA
# ==========================================

df = pd.DataFrame({

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
})

# ==========================================
# 2. CREATE PROFIT / LOSS TARGET
# ==========================================

df["Profit_Amount"] = df["Revenue"] - df["Expenses"]

df["Status"] = np.where(
    df["Profit_Amount"] > 0, 1, 0
)

# 1 = Profit
# 0 = Loss

print(df)

# ==========================================
# 3. SELECT FEATURES AND TARGET
# ==========================================

X = df[[
    "Year",
    "Shoes_Sold",
    "Revenue",
    "Expenses",
    "Marketing_Cost",
    "Returned_Shoes"
]]

y = df["Status"]

# ==========================================
# 4. SPLIT DATA (80/20)
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================================
# 5. CREATE CATBOOST CLASSIFIER
# ==========================================

model = CatBoostClassifier(
    iterations=200,
    learning_rate=0.05,
    depth=4,
    loss_function="Logloss",
    verbose=False,
    random_seed=42
)

# ==========================================
# 6. TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)

# ==========================================
# 7. PREDICTIONS
# ==========================================

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)

print("Predictions:", predictions)
print("Probabilities:", probabilities)

# ==========================================
# 8. MODEL EVALUATION
# ==========================================

print("Accuracy:", accuracy_score(y_test, predictions))

print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

# ==========================================
# 9. FEATURE IMPORTANCE
# ==========================================

importance = model.get_feature_importance()

plt.figure(figsize=(9, 5))

plt.barh(
    X.columns,
    importance,
    color="#36A2EB"
)

plt.title("CatBoost Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()

# ==========================================
# 10. PROFIT VS LOSS SCATTER PLOT
# ==========================================

profit = df[df["Profit_Amount"] > 0]
loss = df[df["Profit_Amount"] <= 0]

plt.figure(figsize=(11, 6))

plt.scatter(
    profit["Year"],
    profit["Profit_Amount"],
    color="#00E676",
    s=120,
    label="Profit",
    edgecolors="white"
)

plt.scatter(
    loss["Year"],
    loss["Profit_Amount"],
    color="#FF5252",
    s=120,
    label="Loss",
    edgecolors="white"
)

plt.plot(
    profit["Year"],
    profit["Profit_Amount"],
    color="#00E676",
    linewidth=2
)

plt.plot(
    loss["Year"],
    loss["Profit_Amount"],
    color="#FF5252",
    linewidth=2
)

plt.axhline(0, color="white", linestyle="--")

plt.title("Shoe Business - Profit vs Loss")
plt.xlabel("Year")
plt.ylabel("Profit / Loss Amount")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ==========================================
# 11. SAVE AND LOAD MODEL
# ==========================================

model.save_model("shoe_catboost_model.cbm")

new_model = CatBoostClassifier()

new_model.load_model("shoe_catboost_model.cbm")

print("Model loaded successfully!")

# ==========================================
# 12. NEW BUSINESS PREDICTION
# ==========================================

new_business = pd.DataFrame({

    "Year": [2027],
    "Shoes_Sold": [750],
    "Revenue": [750000],
    "Expenses": [500000],
    "Marketing_Cost": [60000],
    "Returned_Shoes": [40]

})

result = new_model.predict(new_business)

probability = new_model.predict_proba(new_business)

print("\n2027 BUSINESS PREDICTION:")

print(
    "PROFIT" if result[0] == 1 else "LOSS"
)

print("Loss Probability:", probability[0][0])
print("Profit Probability:", probability[0][1])

# ==========================================
# 13. REGRESSION - REVENUE PREDICTION
# ==========================================

X_reg = df[[
    "Year",
    "Shoes_Sold",
    "Marketing_Cost",
    "Returned_Shoes"
]]

y_reg = df["Revenue"]

Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)

reg_model = CatBoostRegressor(
    iterations=200,
    learning_rate=0.05,
    depth=4,
    verbose=False,
    random_seed=42
)

reg_model.fit(Xr_train, yr_train)

reg_predictions = reg_model.predict(Xr_test)

print("\nREVENUE PREDICTION")

print("MAE:", mean_absolute_error(yr_test, reg_predictions))
print("R2 Score:", r2_score(yr_test, reg_predictions))

# ==========================================
# 14. SAVE REGRESSION MODEL
# ==========================================

reg_model.save_model("shoe_revenue_model.cbm")

print("\nCATBOOST PROJECT COMPLETED!")
