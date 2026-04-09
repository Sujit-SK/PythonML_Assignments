import matplotlib.pyplot as plt

def main():
    print("="*40)
    data = [6, 7, 8, 9, 10, 11, 12]

    n = len(data)

    mean_X = 9
    standardDeviation = 2

    X_mean_X = []
    for i in range(n):
        X_mean_X.append(data[i] - mean_X)
    
    scaledValues = []

    for i in range(n):
        scaledValues.append(X_mean_X[i] / standardDeviation)

    print("="*40)
    print("Before scalling values are : ")
    print(data)
    print("="*40)

    print("="*40)
    print("After scalling values are : ")
    print(scaledValues)
    print("="*40)

    plt.plot(data, scaledValues, marker = "o")
    plt.xlabel("Original Data")
    plt.ylabel("Scaled value (Z-Score)")
    plt.title("Z-Score Scaled Values")

    plt.grid(True)
    plt.show()

if(__name__ == "__main__"):
    main()