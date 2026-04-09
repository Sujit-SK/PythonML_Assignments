from Q1 import Load_csv

def getPassAndFailStudentCount(df):
    PassCount = 0
    FailCount = 0
    StudenCount = 0
    for value in df["FinalResult"]:
        StudenCount = StudenCount + 1
        if(value == 1):
            PassCount = PassCount + 1
        else:
            FailCount = FailCount + 1

    return PassCount, FailCount, StudenCount

def main():
    Border = "-"*50
    df = Load_csv("student_performance_ml.csv")
    print("Dataset gets loaded successfully...")

    PassCount = 0
    FailCount = 0
    StudenCount = 0

    PassCount, FailCount, StudenCount = getPassAndFailStudentCount(df)

    print(Border)
    print("Number of student in dataset.")
    print(StudenCount)

    print(Border)
    print("Number of studen passes.")
    print(PassCount)

    print(Border)
    print("Number of student failed.")
    print(FailCount)

    print(Border)


if(__name__ == "__main__"):
    main()