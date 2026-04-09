import numpy as np

def main():
    print("="*40)
    data = [4, 6, 8, 10, 12]

    n = len(data)
    mean_X = 0.0
    
    sumOfData = 0.0
    for value in data:
        sumOfData = sumOfData + value

    mean_X = sumOfData / n

    print("Mean of Dataset is : ")
    print(mean_X)
    print("="*40)
    DeviationFromMean = []

    for value in data:
        DeviationFromMean.append(value - mean_X)
    
    print("="*40)
    print("Deviation of each value from the mean : ")
    print(list(DeviationFromMean))
    print("="*40)

    X_mean_X_sqr = []

    for i in range(n):
        X_mean_X_sqr.append(DeviationFromMean[i] ** 2)
    
    print("="*40)
    print("Square of Deviation : ")
    print(list(X_mean_X_sqr))
    print("="*40)

    sum_X_mean_X_sqr = 0.0

    for value in X_mean_X_sqr:
        sum_X_mean_X_sqr = sum_X_mean_X_sqr + value

    # Formula : Variance = sum_X_mean_X_sqr / N
    Variance = sum_X_mean_X_sqr / n

    print("="*40)
    print("Variance of dataset is : ")
    print(Variance)
    print("="*40)


if(__name__ == "__main__"):
    main()
