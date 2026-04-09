
import math
import numpy as np

def main():
    Border = "="*40
    X1 = 1
    Y1 = 2000

    X2 = 3
    Y2 = 3000

    X = [1, 3]
    Y = [2000, 3000]
    # Formula for Eculidean distance distance = sqrt((X2 - X1) + (Y2 - Y1))

    distance = (X[1] - X[0]) ** 2 + (Y[1] - Y[0]) ** 2
    distance = math.sqrt(distance)

    print(Border)
    print("Distance before scaling is : ")
    print(distance)
    print(Border)

    n = len(X)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    sum_X_mean_X_sqr = 0.0

    for i in range(n):
        sum_X_mean_X_sqr = sum_X_mean_X_sqr + (X[i] - mean_X) ** 2

    sum_Y_mean_Y_sqr = 0.0

    for i in range(n):
        sum_Y_mean_Y_sqr = sum_Y_mean_Y_sqr + (Y[i] - mean_Y) ** 2

    varianceX = sum_X_mean_X_sqr / n
    varianceY = sum_Y_mean_Y_sqr / n

    print(Border)
    print("Variance of X is : ")
    print(varianceX)
    print(Border)

    print(Border)
    print("Variance of Y is : ")
    print(varianceY)
    print(Border)

    standardDeviationX = math.sqrt(varianceX)
    standardDeviationY = math.sqrt(varianceY)

    print(Border)
    print("Standard Deviation of X is : ")
    print(standardDeviationX)
    print(Border)

    print(Border)
    print("Standard Deviation of Y is : ")
    print(standardDeviationY)
    print(Border)

    scaledValues_X = []
    for i in range(n):
        scaledValues_X.append(float((X[i] - mean_X) / standardDeviationX))

    scaledValues_Y = []
    for i in range(n):
        scaledValues_Y.append(float((Y[i] - mean_Y) / standardDeviationY))

    distance = (scaledValues_X[1] - scaledValues_X[0]) ** 2 + (scaledValues_Y[1] - scaledValues_Y[0]) ** 2
    distance = math.sqrt(distance)

    print(Border)
    print("Distance before scaling is : ")
    print(distance)
    print(Border)

if(__name__ == "__main__"):
    main()