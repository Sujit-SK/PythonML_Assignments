from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def main():

    df = pd.read_csv("student_performance_ml.csv")
    print("Dataset gets loaded successfully...")

    X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    ##############################################################
    # Q1.
    ##############################################################
    model = DecisionTreeClassifier(criterion= "gini", max_depth= 5, random_state=42)

    model = model.fit(X_train, y_train)

    print("Model training compelted.")
    ##############################################################
    # Q2.
    ##############################################################

    result = model.predict(X_test)

    print("Actualy   : ", list(y_test))
    print("Predicted : ", result)


if(__name__ == "__main__"):
    main()