from Q1 import Load_csv
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Border = "-"*50
    df = Load_csv("Student_performance_ml.csv")

    plt.hist(df["StudyHours"], bins=10, edgecolor="black", color="skyblue")
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")
    plt.title("Histogram of StudyHours")

    plt.grid(alpha = 0.3)
    plt.show()



if(__name__ == "__main__"):
    main()