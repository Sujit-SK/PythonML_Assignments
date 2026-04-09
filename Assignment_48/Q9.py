
from sklearn.metrics import classification_report

def main():
    Border = "="*40
    actual =    [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    print(Border)
    print(classification_report(y_true=actual, y_pred=predicted))
    print(Border)

if(__name__ == "__main__"):
    main()