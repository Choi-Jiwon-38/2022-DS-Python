f = open("0919/facebook_combined.txt", "r")

# 친구수 구하기
edges = []

for line in f: # 예시 "1 2"
    # line.split()을 하면 공백을 기준으로 나누어짐 | "1"과 "2" 따로 분리됨
    # split()을 통해 나누어진 x를 int로 변환해준 뒤에 튜플의 형태로 변환 | (1, 2)와 같은 tuple의 형태
    # 튜플 형태로 리스트에 추가
    edges.append(tuple(int(x) for x in line.split()))

num_friends = [0] * 4039 # 사람의 수가 4039명인 것을 사전에 알고 있음

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
# .most_common()을 이용하여 가장 많은 것부터 차례대로 나타남 | 형태는 [(3, 6), (2, 3), (1, 1), (4, 1)]과 같은 형태
# .most_common(1)을 이용하면 가장 많은 것 하나만 나타남 | 형태는 [(3, 6)]
# [0]을 이용하여 접근 -> (3, 6)
# 한 번 더 [0]을 이용하여 가장 많이 나온 수를 구하거나 [1]을 이용하여 그 횟수를 구할 수 있음

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