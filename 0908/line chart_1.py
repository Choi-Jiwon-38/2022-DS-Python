# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.figure(dpi=100) # 해상도를 변경할 경우
plt.plot(years, gdp, marker='^', linestyle=":")
# marker 종류       | 'o' -> 원 | '^' -> 삼각형 | 'x' -> 가위
# linestyle 종류    | dashed(--) | dotted(:) | solid(-)
# custom line      | (0, (2,2)) <- 시작할 위치, (선 긋기, 선 안긋기)
# color는 색상의 이름을 명명하는 것이 아닌 rgb 값을 사용하는 것도 가능
# rgb 값은 (r, g, b)와 #rrggbb 모두 가능

plt.title("Normal GDP")
plt.ylabel("Billions of $")
plt.xlabel("Years")

plt.show()