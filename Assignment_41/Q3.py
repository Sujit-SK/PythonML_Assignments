from Q1 import Ecudistance


def main():
    Border = "-"*40

    df = [
            {'Point':'A', 'X': 2, 'Y': 60, 'Label': 'Fail'},
            {'Point':'B', 'X': 5, 'Y': 80, 'Label': 'Pass'},
            {'Point':'C', 'X': 6, 'Y': 85, 'Label': 'Pass'},
            {'Point':'A', 'X': 1, 'Y': 50, 'Label': 'Fail'}
        ]
    
    print(Border)
    print("Data set created successfully..")
    print(Border)
    
    ##############################################################
    # Step 1 :
    ##############################################################
    print(Border)
    print("Step 1 : Enter a X (Study Hours) and Y (Attendance) Coordinates.")
    print(Border)

    X = float(input("Enter Study Hours : "))
    Y = float(input("Enter Attendance : "))

    print(Border)

    new_point = {'X': X, 'Y': Y}

    print(Border)

    print("new_point is : ", new_point)

    ##############################################################
    # Step 2 :
    ##############################################################
    print(Border)
    print("Step 2 : Extract Eculidean distance from all dataset points.")
    print(Border)

    for value in df:
        value['Distance'] = Ecudistance(new_point, value)

    for value in df:
        print(value)

    ##############################################################
    # Step 2 :
    ##############################################################
    print(Border)
    print("Step 3 : Sort the distance.")
    print(Border)

    sorted_data = sorted(df, key= lambda item : item['Distance'])

    for value in sorted_data:
        print(value)

    ##############################################################
    # Step 4 :
    ##############################################################
    print(Border)
    print("Step 4 : Select K = 3 nearest neighbor.")
    print(Border)

    K = 3

    print("K = ", K)

    nearest = sorted_data[: K]

    for value in nearest:
        print(f"{value['Point']} - Distance - {value['Distance']} ")

    ##############################################################
    # Step 5 :
    ##############################################################
    print(Border)
    print("Step 5 : Predict the class.")
    print(Border)

    votes = {}

    for neighbor in nearest:
        label = neighbor['Label']

        votes[label] = votes.get(label,0) + 1

    predicted_class = max(votes, key=votes.get)

    print(f"Predicted Class of : {X} and {Y} coordinates : ", predicted_class)

if (__name__  == "__main__"):
    main()