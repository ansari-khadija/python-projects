
# 👟 Shoe Business Profit & Loss Analysis
### Machine Learning Projects using XGBoost and CatBoost

## 📌 Project Overview

This project analyzes historical shoe business data to identify profitable and loss-making years using Machine Learning.

Two boosting algorithms are implemented:

1. XGBoost
2. CatBoost

The project also includes data visualization, feature importance, model evaluation, and predictions.

---

## 🚀 Project 1: XGBoost

### Description
XGBoost is used to classify business performance based on historical sales data.

### Features
- Year
- Shoes Sold
- Revenue
- Expenses
- Marketing Cost
- Returned Shoes

### Functions
- Data preprocessing
- Train-test splitting (80/20)
- XGBoost classification
- Profit/Loss prediction
- Accuracy evaluation
- Feature importance
- Profit vs Loss scatter plot
- Model saving and loading
- New business prediction

### Model Output
- 1 = Profit
- 0 = Loss

### Model File
`business_xgboost.pkl`

---

## 🚀 Project 2: CatBoost

### Description
CatBoost is used for business classification and revenue prediction.

### Features
- Historical sales analysis
- Profit and Loss classification
- Revenue prediction
- Feature importance visualization
- Model evaluation

### Functions
- CatBoost classification
- CatBoost regression
- Train-test splitting (80/20)
- Prediction probabilities
- Accuracy evaluation
- MAE and R2 score
- Profit vs Loss scatter plot
- Model saving and loading
- New business prediction

### Model Files
- `shoe_catboost_model.cbm`
- `shoe_revenue_model.cbm`

---

## 📊 Dataset Information

| Column | Description |
|---|---|
| Year | Business year |
| Shoes_Sold | Number of shoes sold |
| Revenue | Total business income |
| Expenses | Total business expenses |
| Marketing_Cost | Advertising cost |
| Returned_Shoes | Returned products |
| Profit_Amount | Revenue - Expenses |
| Status | Profit or Loss |

### Business Classification

- Profit = Revenue > Expenses
- Loss = Revenue < Expenses

---

## 📈 Visualization

Both projects include:

- Profit vs Loss scatter plot
- Year-wise business performance
- Feature importance chart
- Revenue prediction analysis

Color representation:

- 🟢 Green = Profit
- 🔴 Red = Loss

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- CatBoost
- Joblib

---

## 📦 Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn xgboost catboost joblib
```

---

## ▶️ How to Run

1. Clone or download this repository.
2. Install the required libraries.
3. Open the project in Jupyter Notebook or VS Code.
4. Run the XGBoost project.
5. Run the CatBoost project.
6. View the predictions and visualizations.

---


## 🎯 Project Objectives

- Identify profitable and loss-making years.
- Analyze historical business performance.
- Understand important business features.
- Apply boosting algorithms.
- Predict business classifications.
- Estimate future revenue using regression.

---

## ⚠️ Disclaimer

This project uses simulated sample data for educational purposes.

The dataset contains only 15 records and is not suitable for reliable real-world forecasting.

Real business data and larger historical datasets are required for practical deployment.

---

## 👨‍💻 Author
KHADIJA__ANSARI

Machine Learning Practice Project

### ⭐ Algorithms
XGBoost | CatBoost

### 📌 Category
Machine Learning | Data Science | Business Analytics
