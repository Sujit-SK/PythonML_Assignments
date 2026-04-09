import math

def Ecudistance(P1, P2):

    Ans = math.sqrt((P2['X'] - P1['X']) ** 2 + (P2['Y'] - P1['Y']) ** 2)

    return Ans


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
