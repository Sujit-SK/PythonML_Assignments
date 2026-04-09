from Q1 import Ecudistance


def main():
    Border = "-"*40

    df = [
            {'Point':'A', 'X': 1, 'Y': 2, 'Label': 'Red'},
            {'Point':'B', 'X': 2, 'Y': 3, 'Label': 'Red'},
            {'Point':'C', 'X': 3, 'Y': 1, 'Label': 'Blue'},
            {'Point':'A', 'X': 6, 'Y': 5, 'Label': 'Blue'}
        ]
    
    print(Border)
    print("Data set created successfully..")
    print(Border)

    ##############################################################
    # Step 1 :
    ##############################################################
    print(Border)
    print("Step 1 : Enter a X and Y Coordinates.")
    print(Border)

    X = float(input("Enter X Coordinates : "))
    Y = float(input("Enter Y Coordinates : "))

    print(Border)

    new_point = {'X': X, 'Y': Y}

    print(Border)

    print("new_point is : ", new_point)

    for value in df:
        value['Distance'] = Ecudistance(new_point, value)

    sorted_data = sorted(df, key= lambda item : item['Distance'])

    for value in sorted_data:
        print(value)

    ##############################################################
    # Step 2 :
    ##############################################################
    print(Border)
    print("Step 2 : Parameter tuning.")
    print(Border)

    K = 1

    print("K = ", K)

    nearest = sorted_data[: K]

    votes = {}

    for neighbor in nearest:
        label = neighbor['Label']

        votes[label] = votes.get(label,0) + 1

    predicted_class = max(votes, key=votes.get)

    print(f"Predicted Class of : {X} and {Y} coordinates : ", predicted_class)

    K = 3

    print("K = ", K)

    nearest = sorted_data[: K]

    votes = {}

    for neighbor in nearest:
        label = neighbor['Label']

        votes[label] = votes.get(label,0) + 1

    predicted_class = max(votes, key=votes.get)

    print(f"Predicted Class of : {X} and {Y} coordinates : ", predicted_class)

    K = 5

    print("K = ", K)

    nearest = sorted_data[: K]

    votes = {}

    for neighbor in nearest:
        label = neighbor['Label']

        votes[label] = votes.get(label,0) + 1

    predicted_class = max(votes, key=votes.get)

    print(f"Predicted Class of : {X} and {Y} coordinates : ", predicted_class)

    # Why prediction changes when K increase.
    # Ans - K is nearest point that we have take voting for result.
    #  Example - K = 3 means nearest 3 point and within that mejority lable is the predicted class.

if(__name__ == "__main__"):
    main()