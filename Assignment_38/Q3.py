from Q1 import Load_csv

def main():
    Border = "-"*50
    df = Load_csv("Student_performance_ml.csv")

    print(Border)
    print("Average StudyHours")
    print(df["StudyHours"].mean())

    print(Border)
    print("Average Attendance")
    print(df["Attendance"].mean())

    print(Border)
    print("Maximum PreviousScore")
    print(df["PreviousScore"].max())

    print(Border)
    print("Minimum SleepHours")
    print(df["SleepHours"].min())

    print(Border)


if(__name__ == "__main__"):
    main()