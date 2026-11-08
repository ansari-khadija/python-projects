
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
folder = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(folder, "ecommerce_sales.csv"))

# Data cleaning
df = df.drop_duplicates().copy()
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
df = df.dropna(subset=["Order Date", "Order ID"])

# KPI calculations
revenue = df["Sales"].sum()
profit = df["Profit"].sum()
orders = df["Order ID"].nunique()
customers = df["Customer ID"].nunique()

# Theme
sns.set_theme(style="white")
fig = plt.figure(figsize=(17, 14), facecolor="#F5F7FB")

fig.suptitle(
    "E-COMMERCE SALES DASHBOARD",
    fontsize=23,
    fontweight="bold",
    color="#26344A",
    y=0.98
)

gs = fig.add_gridspec(
    4, 2,
    height_ratios=[0.7, 1.5, 1.5, 1.5],
    hspace=0.48,
    wspace=0.25
)

# KPI CARDS
kpi_ax = fig.add_subplot(gs[0, :])
kpi_ax.axis("off")

kpis = [
    ("TOTAL REVENUE", f"${revenue:,.0f}"),
    ("TOTAL PROFIT", f"${profit:,.0f}"),
    ("TOTAL ORDERS", f"{orders:,}"),
    ("CUSTOMERS", f"{customers:,}")
]

for i, (label, value) in enumerate(kpis):
    x = 0.125 + i * 0.25

    kpi_ax.text(
        x, 0.65, value,
        transform=kpi_ax.transAxes,
        fontsize=20,
        fontweight="bold",
        color="#2878B5",
        ha="center"
    )

    kpi_ax.text(
        x, 0.25, label,
        transform=kpi_ax.transAxes,
        fontsize=10,
        color="#68778D",
        ha="center"
    )

# MONTHLY REVENUE
ax1 = fig.add_subplot(gs[1, 0])

monthly = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

ax1.plot(
    monthly.index.astype(str),
    monthly.values,
    color="#3985D6",
    marker="o",
    linewidth=2.5,
    markersize=5
)

ax1.set_title("Monthly Revenue", fontweight="bold", pad=15)
ax1.set_ylabel("Revenue")
ax1.tick_params(axis="x", rotation=45, labelsize=8)
ax1.grid(axis="y", alpha=0.2)
sns.despine(ax=ax1)

# REGIONAL SALES
ax2 = fig.add_subplot(gs[1, 1])

regional = df.pivot_table(
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

regional.plot(
    kind="bar",
    stacked=True,
    ax=ax2,
    colormap="Set2",
    width=0.65
)

ax2.set_title("Regional Sales", fontweight="bold", pad=15)
ax2.set_ylabel("Sales")
ax2.tick_params(axis="x", rotation=0)
ax2.legend(fontsize=8, frameon=False)
sns.despine(ax=ax2)

# DONUT CHART
ax3 = fig.add_subplot(gs[2, 0])

category = df.groupby("Category")["Sales"].sum()

wedges, texts, autotexts = ax3.pie(
    category,
    labels=category.index,
    autopct="%1.1f%%",
    startangle=90,
    pctdistance=0.75,
    wedgeprops={
        "width": 0.42,
        "edgecolor": "white",
        "linewidth": 2
    },
    textprops={"fontsize": 9}
)

ax3.text(
    0, 0,
    f"${revenue:,.0f}",
    ha="center",
    va="center",
    fontsize=13,
    fontweight="bold",
    color="#26344A"
)

ax3.set_title("Category Distribution", fontweight="bold", pad=15)

# HEATMAP
ax4 = fig.add_subplot(gs[2, 1])

sns.heatmap(
    regional,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu",
    linewidths=0.5,
    cbar=False,
    annot_kws={"fontsize": 8},
    ax=ax4
)

ax4.set_title("Regional Performance", fontweight="bold", pad=15)
ax4.tick_params(labelsize=9)

# SCATTER PLOT
ax5 = fig.add_subplot(gs[3, 0])

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Region",
    palette="Set2",
    alpha=0.55,
    s=35,
    ax=ax5
)

ax5.set_title("Sales vs Profit", fontweight="bold", pad=15)
ax5.legend(fontsize=8, frameon=False)
ax5.grid(alpha=0.2)
sns.despine(ax=ax5)

# HISTOGRAM
ax6 = fig.add_subplot(gs[3, 1])

order_sales = df.groupby("Order ID")["Sales"].sum()

sns.histplot(
    order_sales,
    bins=20,
    kde=True,
    color="#3985D6",
    ax=ax6
)

ax6.set_title("Order Value Distribution", fontweight="bold", pad=15)
ax6.set_xlabel("Order Value")
ax6.set_ylabel("Number of Orders")
ax6.grid(axis="y", alpha=0.2)
sns.despine(ax=ax6)

# Final layout
plt.savefig(
    os.path.join(folder, "ecommerce_dashboard.png"),
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()
