import matplotlib.pyplot as plt

friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes) # x축, y축 순서로 입력

# (70, 175)는 a, (65, 170)은 b ... 라벨링을 해주어야 함
# 사용 방법: plt.annotate("넣고 싶은 말", (x좌표, y좌표)
for f, m, l in zip(friends, minutes, labels):
    plt.annotate(l, xy = (f + 0.3, m + 0.3))

plt.show()