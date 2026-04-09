from Q2 import Cal_x_men_x_X_y_mean_y,RegressionEquation
import matplotlib.pyplot as plt

def main():
    Border = "-"*40
    X = [1, 2, 3, 4, 5]
    Y = [20000, 25000, 30000, 35000, 40000]

    mean_X = 0.0
    mean_X_Temp = 0.0

    for value in X:
        mean_X_Temp = mean_X_Temp + value

    mean_X = mean_X_Temp / 5

    mean_Y = 0.0
    mean_Y_Temp = 0.0
    for value in Y:
        mean_Y_Temp = mean_Y_Temp + value
    
    mean_Y = mean_Y_Temp / 5

    print(Border)
    print("mean_X : ", mean_X)
    print("mean_Y : ", mean_Y)

    x_men_x_X_y_mean_y_sum = 0.0

    for i in range(len(X)):
        ret = Cal_x_men_x_X_y_mean_y(X[i], mean_X, Y[i], mean_Y)
        x_men_x_X_y_mean_y_sum = x_men_x_X_y_mean_y_sum + ret

    print(Border)
    print("(X - mean_X) * (Y - mean_Y) : ", x_men_x_X_y_mean_y_sum)

    x_mean_x_sqr = 0.0
    for d in X:
        Ans = (d - mean_X) ** 2
        x_mean_x_sqr = x_mean_x_sqr + Ans

    print(Border)
    print("(X - mean_X)sq : ",x_mean_x_sqr)

    m = x_men_x_X_y_mean_y_sum / x_mean_x_sqr

    print(Border)
    print("Slop of (m) : ", m)

    # mean_Y = m * mean_X + C

    C = mean_Y - m * mean_X

    print(Border)
    print("Intercept of (c) : ", C)

    Experience = int(input("Enter experiance in years to predict a salary : "))
    new_point = [[Experience]]

    YP = RegressionEquation(m, Experience, C)

    print(Border)
    print(f"Predicted Salary for {Experience} Years Experience : ", YP)

    plt.scatter(X, Y, color = 'blue')
    plt.plot(X, Y, color = 'red')
    plt.xlabel("Independent variable (X)")
    plt.ylabel("Dependent Variable (Y)")
    plt.title("Linear Regression.")

    plt.show()


if(__name__ == "__main__"):
    main()