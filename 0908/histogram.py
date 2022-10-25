import matplotlib.pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

xs = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
xs = [i + 5 for i in xs]
count = [2, 0, 0, 0, 0, 0, 1, 3, 4, 3]

plt.bar(xs, count, width = 10, edgecolor="black")
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.show()