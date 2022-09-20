f = open("0919/facebook_combined.txt", "r")

# 친구수 구하기
edges = []

for line in f:
    edges.append(tuple(int(x) for x in line.split()))

num_friends = [0] * 4039

for u, v in edges:
    num_friends[u] += 1
    num_friends[v] += 1

# mean 평균
mean = sum(num_friends) / len(num_friends)
print(f"mean: {mean}")

# median 중앙값
num_friends_sorted = sorted(num_friends)
median = num_friends_sorted[len(num_friends_sorted) // 2]
print(f"median: {median}")

# min 최솟값
minval = min(num_friends)
print(f"min: {minval}")

# max 최댓값
maxval = max(num_friends)
print(f"max: {maxval}")

# mod 최빈값
from collections import Counter
cnt = Counter(num_friends)
print(f"mod: {cnt.most_common(1)[0][0]}")

# quantile 분위
q25 = num_friends_sorted[int(len(num_friends_sorted) * 0.25)]
q50 = num_friends_sorted[int(len(num_friends_sorted) * 0.5)]
q75 = num_friends_sorted[int(len(num_friends_sorted) * 0.75)]
print(f"q25: {q25}")
print(f"q25: {q50}")
print(f"q25: {q75}")


# 산포도 -----------
# max - min
minmax = maxval - minval
print(f"minmax: {minmax}")

# varience & standard deviation
var = sum((x - mean) ** 2 for x in num_friends)
print(f"var: {var}")
print(f"stddev: {var ** 0.5}")

# iqr
print(f"iqr: {q75 - q25}")


# 히스토그램
cnt = Counter([x // 10 * 10 for x in num_friends])

keys, values = zip(*cnt.items()) # key 값과 value 값을 분리

import matplotlib.pyplot as plt
plt.bar(keys, values, width = 10, edgecolor = "black")
plt.show()