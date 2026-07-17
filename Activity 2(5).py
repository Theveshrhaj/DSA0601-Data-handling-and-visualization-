import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

energy = [420, 450, 490, 530, 560, 600, 580, 590, 610, 630, 590, 540]

plt.figure(figsize=(10,5))
plt.plot(months, energy, marker='o')

plt.title("Monthly Electricity Generation (2025)")
plt.xlabel("Months")
plt.ylabel("Energy Generated (MWh)")
plt.grid(True)

plt.show()

print("Highest Energy Production:", max(energy), "MWh in", months[energy.index(max(energy))])
print("Lowest Energy Production:", min(energy), "MWh in", months[energy.index(min(energy))])
