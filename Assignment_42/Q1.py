
def Cal_x_men_x_X_y_mean_y(x, mean_x, y, mean_y):

    Ans = (x - mean_x) * (y - mean_y)

    return Ans


def main():
    Border = "-"*40

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print(Border)
    print("Data set created successfully..")
    print(Border)

    ##############################################################
    # Step 1 : Calculate Mean of X (mean_X)
    ##############################################################
    print(Border)
    print("Step 1 : Calculate Mean of X (mean_X)")
    print(Border)

    mean_X = 0.0
    mean_X_Temp = 0.0

    for d in X:
        mean_X_Temp = mean_X_Temp + d
    
    mean_X = mean_X_Temp / 5
    print("Mean of X is : ", mean_X)

    ##############################################################
    # Step 2 : Calculate Mean of Y (mean_Y)
    ##############################################################
    print(Border)
    print("Step 2 : Calculate Mean of Y (mean_Y)")
    print(Border)

    mean_Y = 0.0
    mean_Y_Temp = 0.0

    for d in Y:
        mean_Y_Temp = mean_Y_Temp + d
    
    mean_Y = mean_Y_Temp / 5
    print("Mean of Y is : ", mean_Y)

    ##############################################################
    # Step 3 : Calculate Slop (m)
    ##############################################################
    print(Border)
    print("Step 3 : Calculate Slop (m)")
    print(Border)

    x_men_x_X_y_mean_y = []

    for i in range(len(X)):
        ret = Cal_x_men_x_X_y_mean_y(X[i], mean_X, Y[i], mean_Y)
        x_men_x_X_y_mean_y.append(ret)

    x_men_x_X_y_mean_y_sum = 0.0
    for d in x_men_x_X_y_mean_y:
        x_men_x_X_y_mean_y_sum = x_men_x_X_y_mean_y_sum + d
 
    x_mean_x_sqr = 0.0
    for d in X:
        Ans = (d - mean_X) ** 2
        x_mean_x_sqr = x_mean_x_sqr + Ans

    m = x_men_x_X_y_mean_y_sum / x_mean_x_sqr

    print("Slop of (m) : ", m)

    ##############################################################
    # Step 4 : Calculate Intercept (c)
    ##############################################################
    print(Border)
    print("Step 3 : Calculate Intercept (c)")
    print(Border)

    # mean_Y = m + mean_X + C
    # 3.6 = 0.4 * 3.0 + C
    # 3.6 = 1.2 + C
    # C = 3.6 - 1.2
    # C = 2.4

    C = mean_Y - m * mean_X

    print("Intercept of (c) : ", C)

    ##############################################################
    # Step 4 : Regression Equation
    ##############################################################
    print(Border)
    print("Step 4 : Regression Equation")
    print(Border)

    new_X = float(input("Enter X for predict Y : "))

    print("X = ", new_X)

    Predicted_Y = m * new_X + C

    print(f"predicted Y for X = {new_X} : ", Predicted_Y)

    print(Border)



    
if(__name__ == "__main__"):
    main()
