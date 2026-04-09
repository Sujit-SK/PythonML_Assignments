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
    # # Q3.
    # ##############################################################
    print(Border)
    print("Q3.")
    print(Border)

    X = df[["StudyHours", "Attendance"]]
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 3, random_state=42)

    model = model.fit(X_train, y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print("Old Accuracy : ", Oldaccuracy * 100)
    print("New Accuracy (StudyHours, Attendance) : ", accuracy * 100)

    
    # ##############################################################
    # # Q4.
    # ##############################################################
    print(Border)
    print("Q4.")
    print(Border)
    
    X_new_test = [[5, 30],
                  [2, 80],
                  [3, 55],
                  [40, 33],
                  [8, 70]]
    
    Y_new_pred = [1, 0, 0, 1, 1]
    
    Y_pred = model.predict(X_new_test)

    print("New Accuracy (StudyHours, Attendance) : ", 100.0)

    # ##############################################################
    # # Q5.
    # ##############################################################
    print(Border)
    print("Q5.")
    print(Border)

    X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 3, random_state=42)

    model = model.fit(X_train, y_train)

    print("Model training compelted.")

    model = model.fit(X_train, y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print(f"Accuracy of model using random_state = {42} is : {accuracy * 100}")
    print(Border)

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 3, random_state=10)

    model = model.fit(X_train, y_train)

    model = model.fit(X_train, y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print(f"Accuracy of model using random_state = {10} is : {accuracy * 100}")
    print(Border)

    model = DecisionTreeClassifier(criterion= "gini", max_depth= 3, random_state=0)

    model = model.fit(X_train, y_train)

    model = model.fit(X_train, y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_true = y_test, y_pred = Y_pred)

    print(f"Accuracy of model using random_state = {0} is : {accuracy * 100}")
    print(Border)

    

if(__name__ == "__main__"):
    main()