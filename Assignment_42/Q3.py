from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    X = [[1], [2], [3], [4], [5]]
    Y = [20000, 25000, 30000, 35000, 40000]

    model = LinearRegression()

    model.fit(X, Y)

    Y_pred = model.predict(X)

    Experience = int(input("Enter experiance in years to predict a salary : "))
    new_point = [[Experience]]
    result = model.predict(new_point)

    print(f"Predicted Salary for {Experience} Years Experience : ",result)

    plt.scatter(X, Y, color = 'blue')
    plt.plot(X, Y_pred, color = 'red')
    plt.xlabel("Independent variable (X)")
    plt.ylabel("Dependent Variable (Y)")
    plt.title("Linear Regression.")

    plt.show()

if(__name__ == "__main__"):
    main()