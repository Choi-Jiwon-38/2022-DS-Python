from audioop import bias
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]

# xs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
xs = range(len(variance))

plt.plot(xs, variance, "^:", label="variance")
plt.plot(xs, bias_squared, "-o", label="bias^2")
plt.plot(xs, total_error, "x:r", label="total error") # marker, linestyle, color를 한꺼번에 설정할 수 있음.

plt.legend(loc="upper center")

plt.xlabel("model complexity")
plt.xticks([0, 8]) # 0과 8만 표시하고 싶은 경우
plt.xticks([0, 8], ["Min", "Max"])

plt.title("The Bias-Variance Tradeoff")

plt.show()
