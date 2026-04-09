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

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 3, random_state=42)

    model = model.fit(X_train, y_train)

    print("Model training compelted.")

    model = model.fit(X_train, y_train)

    Y_pred = model.predict(X_test)

    Oldaccuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    counter = 0
    for value in model.feature_importances_:
        print(f"{X.columns[counter]} Score is : {value}")
        counter = counter + 1
    print(Border)

    maxScore = 0.0

    index = 0
    tempcount = 0
    for value in model.feature_importances_:
        tempcount = tempcount + 1
        if(value > maxScore):
            maxScore = value
            index = tempcount
    
    print(f"Contributes the most in prediction Final Result => {X.columns[index]} : {maxScore}")
    print(Border)

    minScore = 0.0
    index = 0
    tempcount = 0
    for value in model.feature_importances_:
        tempcount = tempcount + 1
        if(value < minScore):
            minScore = value
            index = tempcount

    print(f"Contributes the least in prediction Final Result => {X.columns[index]} : {minScore}")
    print(Border)
    
    ##############################################################
    # Q2.
    ##############################################################
    print(Border)
    print("Q2.")
    print(Border)
    
    X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]]
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 3, random_state=42)

    model = model.fit(X_train, y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print("Accuracy of model without (SleepHours) in percentage is : ",accuracy * 100)

    print("Old Accuracy : ", Oldaccuracy * 100)
    print("New Accuracy : ", accuracy * 100)

    # Conclusion Removing SleepHours column dosent effect accuracy of model.

    # ##############################################################
    # # Q4.
    # ##############################################################
    # print(Border)
    # print("Q4.")
    # print(Border)

    # cm = confusion_matrix(y_true= y_test, y_pred= Y_pred)

    # data = ConfusionMatrixDisplay(cm, display_labels=model.classes_)

    # data.plot()
    # plt.title("ConfusionMatrixDisplay")
    # plt.show()

    # # Actualy   :  [1, 0, 0, 0, 0, 0]
    # # Predicted :  [1, 0, 0, 0, 0, 0]

    # # 1 = Positive
    # # 2 = Negative

    # # Explaination

    # # TP (True Positive) = Actualy = 1 and Predicted = 1
    # # Total TP = 1

    # # TN (True Negative) = Actualy = 1 and Predicted = 0
    # # Total TN = 0

    # # FP (False Positive) = Actualy = 0 and Predicted = 1
    # # Total FP = 0

    # # FN (False Negative) = Actualy = 0 and predicted = 0
    # # Total FN = 5

    # ##############################################################
    # # Q5.
    # ##############################################################
    # print(Border)
    # print("Q5.")
    # print(Border)

    # train_accuracy = model.score(X_train, y_train)
    # print("Training Accuracy : ", train_accuracy * 100)

    # test_accuracy = model.score(X_test, y_test)
    # print("Testing Accuracy : ", test_accuracy * 100)

    # print("Model is overfiting.")

    # ##############################################################
    # # Q6.
    # ##############################################################
    # print(Border)
    # print("Q6.")
    # print(Border)
    
    # new_data = [[6, 85, 66, 7, 7]]

    # myPredict = model.predict(new_data)

    # if(myPredict == 1):
    #     print("Studen will pass.")
    # else:
    #     print("Studen will fail.")

if(__name__ == "__main__"):
    main()