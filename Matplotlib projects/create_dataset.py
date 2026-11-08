
import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 1000

categories = ["Electronics", "Furniture", "Fashion", "Accessories"]
products = [
    "Laptop", "Mobile", "Tablet",
    "Chair", "Table", "Sofa",
    "Shoes", "Jackets", "Shirts",
    "Watch", "Bag", "Headphones"
]

regions = ["East", "West", "North", "South"]

customers = [
    f"CUST{i:03d}" for i in range(1, 201)
]

df = pd.DataFrame({
    "Order ID": [f"ORD{i:04d}" for i in range(1, n + 1)],
    "Order Date": np.random.choice(
        pd.date_range("2024-01-01", "2025-12-31"), n
    ),
    "Customer ID": np.random.choice(customers, n),
    "Product Name": np.random.choice(products, n),
    "Category": np.random.choice(categories, n),
    "Region": np.random.choice(regions, n),
    "Sales": np.random.randint(100, 5000, n),
    "Quantity": np.random.randint(1, 10, n),
    "Discount": np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20], n
    )
})

df["Profit"] = (
    df["Sales"] *
    (1 - df["Discount"]) *
    np.random.uniform(0.10, 0.30, n)
).round(2)

# Save CSV in the same folder as this Python file
folder = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(folder, "ecommerce_sales.csv")

df.to_csv(file_path, index=False)

print("SUCCESS! Dataset created.")
print("File location:", file_path)
print("Total records:", len(df))
print(df.head())
