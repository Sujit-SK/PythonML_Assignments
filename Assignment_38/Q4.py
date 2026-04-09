from Q1 import Load_csv

def main():
    Border = "-"*50
    df = Load_csv("Student_performance_ml.csv")

    value = df["FinalResult"].value_counts()

    PassPercentage = 0.0
    FailPercentage = 0.0
    for key, value in value.items():
        if(key == 1):
            PassPercentage = value / df["FinalResult"].count() * 100
        else:
            FailPercentage = value / df["FinalResult"].count() * 100

    print(Border)
    print("Percentage of pass student:")
    print(PassPercentage)

    print(Border)
    print("Percentage of fail student:")
    print(FailPercentage)

    print(Border)


if(__name__ == "__main__"):
    main()