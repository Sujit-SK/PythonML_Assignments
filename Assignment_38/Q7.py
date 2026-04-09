from Q1 import Load_csv
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Border = "-"*50
    df = Load_csv("Student_performance_ml.csv")

    sns.scatterplot(df)
    plt.show()



if(__name__ == "__main__"):
    main()