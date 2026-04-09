
from sklearn.metrics import confusion_matrix, accuracy_score

def main():
    Border = "="*40
    actual =    [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    confusionmatrix = confusion_matrix(y_true=actual, y_pred=predicted)
    accuracy = accuracy_score(y_true=actual, y_pred=predicted)

    print(Border)
    print("Using Default function")
    print(confusionmatrix)
    print(accuracy * 100)
    print(Border)


    TP = 0
    TN = 0
    FP = 0
    FN = 0
    n = len(actual)

    # 1 - Positive
    # 0 - Negative

    for i in range(n):
        if(actual[i] == 1):
            if(actual[i] == predicted[i]):
                TP = TP + 1
            else:
                FN = FN + 1
        elif(actual[i] == 0):
            if(actual[i] == predicted[i]):
                TN = TN + 1
            else:
                FP = FP + 1

    print(Border)   
    print("Using User define logic")    
    print("TP : ", TP)
    print("TN : ", TN)
    print("FP : ", FP)
    print("FN : ", FN)

    accuracy = (TP + TN) / (TP + TN + FP + FN)

    print(accuracy * 100)
    print(Border)

if(__name__ == "__main__"):
    main()