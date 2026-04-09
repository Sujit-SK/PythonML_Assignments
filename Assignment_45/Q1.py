import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

def main():
    Border = "-"*40
    #--------------------------------------------
    # Step 1 : Load dataset
    #--------------------------------------------
    print(Border)
    print("Step 1 : Load dataset")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    print("Few records from the dataset. : ")
    print(df.head())

    #--------------------------------------------
    # Step 2 : Clean Prepare and maipulate data
    #-------------------------------------------- 
    print(Border)
    print("Step 2 : Clean Prepare and maipulate data")
    print(Border)

    print("------Clean unnamed columns-------\n")

    print("Shape of data set before removing : ", df.shape)

    if('Unnamed: 0' in df.columns):
        df.drop(columns='Unnamed: 0', inplace=True)


    df.dropna(inplace=True)
    print("Total records : ", df.shape[0])
    print("Total column : ", df.shape[1])

    #--------------------------------------------
    # Step 3 : Train Data
    #-------------------------------------------- 
    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train, Y_train)

    #--------------------------------------------
    # Step 4 : Test Data
    #-------------------------------------------- 
    print(Border)
    print("Step 4 : Test Data")
    print(Border)

    Y_pred = model.predict(X_test)

    #--------------------------------------------
    # Step 5 : Display Predicted values
    #-------------------------------------------- 
    print(Border)
    print("Step 5 : Display Predicted values")
    print(Border)

    print("Actual : ", list(Y_test))
    print("Predicted : ", list(Y_pred))

if(__name__ == "__main__"):
    main()
