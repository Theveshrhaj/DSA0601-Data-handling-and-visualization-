import matplotlib.pyplot as plt

categories = [
    "Groceries", "Dairy", "Fruits", "Vegetables", "Bakery",
    "Beverages", "Snacks", "Personal Care",
    "Household Items", "Frozen Foods"
]

sales = [120, 95, 80, 75, 68, 90, 110, 55, 70, 60]

plt.figure(figsize=(10,6))
plt.bar(categories, sales)

plt.title("Monthly Sales Revenue by Product Category (June 2026)")
plt.xlabel("Product Category")
plt.ylabel("Sales (Lakhs)")
plt.xticks(rotation=45)

plt.show()

# Highest and Lowest
highest = max(sales)
lowest = min(sales)

print("Highest Selling Category:", categories[sales.index(highest)], "-", highest, "Lakhs")
print("Lowest Selling Category:", categories[sales.index(lowest)], "-", lowest, "Lakhs")
