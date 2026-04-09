import numpy as np
import math
import matplotlib.pyplot as plt
def main():
    Border = "="*40
    X = [
        [25, 30, 35],
        [20000, 40000, 80000]
    ]
    print(Border)
    print("Before scaled : ")
    print(X)
    print(Border)

    X1 = X[0]
    X2 = X[1]
    n = len(X[0])
    mean_X1 = np.mean(X1)
    mean_X2 = np.mean(X2)

    print(Border)
    print("Mean of X1 is : ", mean_X1)
    print("Mean of X2 is : ", mean_X2)
    print(Border)

    sum_X1_meanX1_sqr = 0.0

    for i in range(n):
        sum_X1_meanX1_sqr = sum_X1_meanX1_sqr + (X1[i] - mean_X1) ** 2

    sum_X2_meanX2_sqr = 0.0

    for i in range(n):
        sum_X2_meanX2_sqr = sum_X2_meanX2_sqr + (X2[i] - mean_X2) ** 2


    VarianceX1 = sum_X1_meanX1_sqr / n
    VarianceX2 = sum_X2_meanX2_sqr / n

    print(Border)
    print("Variance of X1 is : ", VarianceX1)
    print("Variance of X2 is : ", VarianceX2)
    print(Border)

    StandardDeviationX1 = math.sqrt(VarianceX1)
    StandardDeviationX2 = math.sqrt(VarianceX2)

    print(Border)
    print("Standard Deviation of X1 is : ", StandardDeviationX1)
    print("Standard Deviation of X2 is : ", StandardDeviationX2)
    print(Border)

    scaled_valuesX1 = []

    for i in range(n):
        scaled_valuesX1.append(float((X1[i] - mean_X1) / StandardDeviationX1))
    
    scaled_valuesX2 = []

    for i in range(n):
        scaled_valuesX2.append(float((X2[i] - mean_X2) / StandardDeviationX2))
    

    scaled_dataset = [scaled_valuesX2, scaled_valuesX2]

    print(Border)
    print("Scaled Dataset : ")
    print(scaled_dataset)
    print(Border)

    plt.figure()

    plt.plot(X1, marker='o', label="X1")
    plt.plot(X2, marker='o', label="X2")

    plt.title("Before Scaling")
    plt.legend()
    plt.grid(True)

    plt.show()


    plt.figure()

    plt.plot(scaled_dataset[0], marker='o', label="scaled_X1")
    plt.plot(scaled_dataset[1], marker='o', label="scaled_X2")

    plt.title("After Standardization (Z-score)")
    plt.legend()
    plt.grid(True)

    plt.show()

plt.show()
if(__name__ == "__main__"):
    main()