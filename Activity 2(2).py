import matplotlib.pyplot as plt

salary = [3.2, 4.5, 5.0, 6.8, 7.2, 8.5, 4.8, 5.5, 6.0, 7.8, 9.2, 10.5]

plt.figure(figsize=(8,5))
plt.hist(salary, bins=5)

plt.title("Distribution of Salary Packages")
plt.xlabel("Salary Package (LPA)")
plt.ylabel("Number of Students")

plt.show()
