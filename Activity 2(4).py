import matplotlib.pyplot as plt

advertising = [5, 8, 10, 12, 15, 18, 20, 22, 25, 28]
sales = [42, 55, 63, 70, 82, 91, 98, 110, 120, 132]

plt.figure(figsize=(8,5))
plt.scatter(advertising, sales)

plt.title("Advertising Cost vs Sales Revenue")
plt.xlabel("Advertising Cost (Lakhs)")
plt.ylabel("Sales Revenue (Lakhs)")

plt.show()
