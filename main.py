"""
Week 4 Project
E-Commerce Sales Analysis and Data Visualization

Intern : Mallikarjun Revi
Language : Python
Libraries : Pandas, Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------
# Create Output Folders
# -------------------------------------------------

os.makedirs("visualizations", exist_ok=True)
os.makedirs("report", exist_ok=True)

print("=" * 70)
print("            E-COMMERCE SALES ANALYSIS PROJECT")
print("=" * 70)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

try:
    df = pd.read_csv("data/sales_data.csv")
    print("\nDataset Loaded Successfully.")
except FileNotFoundError:
    print("\nError: Dataset not found.")
    print("Please place 'sales_data.csv' inside the 'data' folder.")
    exit()

# -------------------------------------------------
# Dataset Overview
# -------------------------------------------------

print("\nDATASET OVERVIEW")
print("-" * 70)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nFirst Five Records")
print(df.head())

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

# -------------------------------------------------
# Missing Values
# -------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

df.fillna(0, inplace=True)

# -------------------------------------------------
# Duplicate Records
# -------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Records : {duplicates}")

df.drop_duplicates(inplace=True)

# -------------------------------------------------
# Convert Date Column
# -------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------------------------
# Business Analysis
# -------------------------------------------------

print("\nBUSINESS ANALYSIS")
print("-" * 70)

total_revenue = df["Total_Sales"].sum()
average_sale = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

best_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

print(f"Total Revenue        : ₹{total_revenue:,.2f}")
print(f"Average Sale         : ₹{average_sale:,.2f}")
print(f"Highest Sale         : ₹{highest_sale:,.2f}")
print(f"Lowest Sale          : ₹{lowest_sale:,.2f}")
print(f"Best Selling Product : {best_product}")

# -------------------------------------------------
# Revenue by Product
# -------------------------------------------------

product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product")
print(product_sales)

# -------------------------------------------------
# Revenue by Region
# -------------------------------------------------

region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
)

print("\nRevenue by Region")
print(region_sales)

# -------------------------------------------------
# Monthly Sales Trend
# -------------------------------------------------

monthly_sales = (
    df.groupby("Date")["Total_Sales"]
    .sum()
    .sort_index()
)

# -------------------------------------------------
# Visualization 1 - Bar Chart
# -------------------------------------------------

plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/bar_chart.png")

plt.close()

# -------------------------------------------------
# Visualization 2 - Pie Chart
# -------------------------------------------------

plt.figure(figsize=(7, 7))

region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.ylabel("")
plt.title("Sales Distribution by Region")

plt.tight_layout()

plt.savefig("visualizations/pie_chart.png")

plt.close()

# -------------------------------------------------
# Visualization 3 - Line Chart
# -------------------------------------------------

plt.figure(figsize=(10, 5))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/line_chart.png")

plt.close()

# -------------------------------------------------
# Generate Report
# -------------------------------------------------

with open("report/sales_report.txt", "w") as file:

    file.write("E-COMMERCE SALES ANALYSIS REPORT\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Total Revenue        : ₹{total_revenue:,.2f}\n")
    file.write(f"Average Sale         : ₹{average_sale:,.2f}\n")
    file.write(f"Highest Sale         : ₹{highest_sale:,.2f}\n")
    file.write(f"Lowest Sale          : ₹{lowest_sale:,.2f}\n")
    file.write(f"Best Selling Product : {best_product}\n\n")

    file.write("Revenue by Product\n")
    file.write("-" * 30 + "\n")
    file.write(product_sales.to_string())
    file.write("\n\n")

    file.write("Revenue by Region\n")
    file.write("-" * 30 + "\n")
    file.write(region_sales.to_string())

print("\nCharts Saved Successfully.")
print("Report Generated Successfully.")

print("\nFiles Created:")
print("✔ report/sales_report.txt")
print("✔ visualizations/bar_chart.png")
print("✔ visualizations/pie_chart.png")
print("✔ visualizations/line_chart.png")

print("\nProject Completed Successfully!")
print("=" * 70)