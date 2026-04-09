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

    df = pd.read_csv("PlayPredictor.csv")

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

    print("Shape of data set after removing : ", df.shape)

    print("--------- Label Encoding ---------\n")

    df['Whether'] = df['Whether'].astype('category').cat.codes
    df['Temperature'] = df['Temperature'].astype('category').cat.codes

    print(df.head())

    #--------------------------------------------
    # Step 3 : Train Data
    #-------------------------------------------- 
    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    K = 3

    model = KNeighborsClassifier(n_neighbors=K)

    model.fit(X, Y)
    new_data = [[2,0]]

    new_data_pred = model.predict(new_data)

    print("Prediction is : ",new_data_pred[0])

    #--------------------------------------------
    # Step 4 : Calculate Accuracy
    #-------------------------------------------- 
    print(Border)
    print("Step 4 : Calculate Accuracy")
    print(Border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

    accuracy_Scores = []

    for i in range(1, 11, 1):
        model = KNeighborsClassifier(n_neighbors=i)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_Scores.append(accuracy)
    
    
    K = 1
    for Value in accuracy_Scores:
        print(f"K = {K} Accuracy is {Value}")
        K = K + 1

    print(Border)

    max_accuracy_score = 0.0
    Best_K_index = 0
    for i in range(0, len(accuracy_Scores), 1):

        if(accuracy_Scores[i] > max_accuracy_score):
            max_accuracy_score = accuracy_Scores[i]
            Best_K_index = i + 1

    print("Best K value is : ",Best_K_index)

if(__name__ == "__main__"):
    main()
