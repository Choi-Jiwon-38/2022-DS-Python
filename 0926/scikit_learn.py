from statistics import linear_regression
from sklearn.linear_model import LinearRegression

x = [[1, 2], [3, 2], [3, 7], [1, 1], [1, 0]]
y = [[4], [8], [23], [1], [-2]]

model = LinearRegression()
model.fit(x, y)

print(model.coef_)      #w 에 해당하는 값
print(model.intercept_) #b 에 해당하는 값

x_test = [[5, 10]]
y_test= model.predict(x_test)
print(y_test)