import numpy as np
import math

def main():
    Border = "="*40
    data = [6, 7, 8, 9, 10, 11, 12]

    n = len(data)
    mean_data = np.mean(data)

    print(Border)
    print("Mean of dataset is : ")
    print(mean_data)
    print(Border)

    sum_X_mean_data_sqr = 0.0

    for i in range(n):
        sum_X_mean_data_sqr = sum_X_mean_data_sqr + (data[i] - mean_data) ** 2

    Variance = sum_X_mean_data_sqr / n

    print(Border)
    print("Variance is : ")
    print(Variance)
    print(Border)

    standardDeviation = math.sqrt(Variance)

    print(Border)
    print("Standard Deviation is : ")
    print(standardDeviation)
    print(Border)

if(__name__ == "__main__"):
    main()