from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
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

    Y_pred = model.predict(X_test)

    print("Actualy   : ", list(y_test))
    print("Predicted : ", Y_pred)

    ##############################################################
    # Q3.
    ##############################################################

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print("Accuracy of model in percentage is : ",accuracy * 100)


if(__name__ == "__main__"):
    main()