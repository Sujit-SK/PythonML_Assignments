from sklearn.linear_model import LinearRegression
import numpy as np

def main():
    Border = "-"*40
    StudyHours = np.array([[1], [2], [3], [4], [5]])
    Markes = np.array([50, 55, 60, 65, 70])

    X = StudyHours
    Y = Markes

    model = LinearRegression()
    model.fit(X, Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    x_mean_X = []

    for value in X:
        Ans = value - mean_X
        x_mean_X.append(Ans)

    y_mean_Y = []

    for value in Y:
        Ans = value - mean_Y
        y_mean_Y.append(Ans)

    sum_x_mean_X_X_y_mean_Y = 0.0
    for i in range(len(X)):
        Ans = x_mean_X[i] * y_mean_Y[i]
        sum_x_mean_X_X_y_mean_Y = sum_x_mean_X_X_y_mean_Y + Ans


    sum_X_Mean_X_sqr = 0.0
    for value in x_mean_X:
        Ans = value ** 2
        sum_X_Mean_X_sqr = sum_X_Mean_X_sqr + Ans

    m = sum_x_mean_X_X_y_mean_Y / sum_X_Mean_X_sqr
    print(Border)
    print("UserDefine Coefficient is : ", m)

    # Intercept formula mean_Y = m * mean_Y + c

    Ans = m * mean_X
    C = mean_Y - Ans

    print("UserDefine Intercept is : ", C)
    print(Border)

    print(Border)
    print("Coefficient is : ", model.coef_)
    print("Intercept is : ", model.intercept_)
    print(Border)

if(__name__ == "__main__"):
    main()
