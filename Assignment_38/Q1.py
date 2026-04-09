import pandas as pd

def Load_csv(DatasetName):
    df = pd.read_csv(DatasetName)
    return df

def main():
    Border = "-"*50
    df = Load_csv("student_performance_ml.csv")
    print("Dataset gets loaded successfully...")

    print(Border)
    print("First 5 Records.")
    print(df.head())
    print(Border)

    print(Border)
    print("Last 5 Records.")
    print(df.tail())
    print(Border)

    print(Border)
    print("Total number rows and columns")
    print(df.shape)
    print(Border)

    print(Border)
    print("Data types of each column")
    for column in df.columns:
        print(df[column].dtype)
    print(Border)

if(__name__ == "__main__"):
    main()
