import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(movies, num_oscars, width = 0.2, edgecolor="black")
# width 속성은 막대의 두께를 설정
# edgecolor 속성은 막대의 테두리 색상을 설정

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

plt.show()