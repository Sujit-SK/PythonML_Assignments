from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

def main():
    Border = "-"*40
    df = pd.read_csv("student_performance_ml.csv")
    print("Dataset gets loaded successfully...")

    X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    ##############################################################
    # Q1.
    ##############################################################
    print(Border)
    print("Q1.")
    print(Border)

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 5, random_state=42)

    model = model.fit(X_train, y_train)

    print("Model training compelted.")

    ##############################################################
    # Q2.
    ##############################################################
    print(Border)
    print("Q2.")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Actualy   : ", list(y_test))
    print("Predicted : ", Y_pred)

    ##############################################################
    # Q3.
    ##############################################################
    print(Border)
    print("Q3.")
    print(Border)

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print("Accuracy of model in percentage is : ",accuracy * 100)

    ##############################################################
    # Q4.
    ##############################################################
    print(Border)
    print("Q4.")
    print(Border)

    cm = confusion_matrix(y_true= y_test, y_pred= Y_pred)

    data = ConfusionMatrixDisplay(cm, display_labels=model.classes_)

    data.plot()
    plt.title("ConfusionMatrixDisplay")
    plt.show()

    # Actualy   :  [1, 0, 0, 0, 0, 0]
    # Predicted :  [1, 0, 0, 0, 0, 0]

    # 1 = Positive
    # 2 = Negative

    # Explaination

    # TP (True Positive) = Actualy = 1 and Predicted = 1
    # Total TP = 1

    # TN (True Negative) = Actualy = 1 and Predicted = 0
    # Total TN = 0

    # FP (False Positive) = Actualy = 0 and Predicted = 1
    # Total FP = 0

    # FN (False Negative) = Actualy = 0 and predicted = 0
    # Total FN = 5

    ##############################################################
    # Q5.
    ##############################################################
    print(Border)
    print("Q5.")
    print(Border)

    train_accuracy = model.score(X_train, y_train)
    print("Training Accuracy : ", train_accuracy * 100)

    test_accuracy = model.score(X_test, y_test)
    print("Testing Accuracy : ", test_accuracy * 100)

    print("Model is overfiting.")

if(__name__ == "__main__"):
    main()