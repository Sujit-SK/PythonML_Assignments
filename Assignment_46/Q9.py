from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def main():
    Border = "-"*40
    StudyHours = np.array([1, 2, 3, 4, 5])
    SleepHours = np.array([1, 2, 3, 4, 5])
    Markes = np.array([50, 55, 60, 65, 70])

    df = pd.DataFrame({
        'StudyHours': StudyHours,
        'SleepHours': SleepHours,
        'Markes': Markes
    })

    X = df[['StudyHours', 'SleepHours']]
    Y = df['Markes']

    model = LinearRegression()
    model.fit(X, Y)

    print(Border)
    print("Coefficient is : ", model.coef_)
    print("Intercept is : ", model.intercept_)
    print(Border)

if(__name__ == "__main__"):
    main()