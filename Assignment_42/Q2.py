
def Cal_x_men_x_X_y_mean_y(x, mean_x, y, mean_y):

    Ans = (x - mean_x) * (y - mean_y)

    return Ans

def RegressionEquation(m, new_X, C):
    Ans = m * new_X + C
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
    # Step 5 : Predict All Y values using Regression Equation
    ##############################################################
    print(Border)
    print("Step 5 : Predict All Y values using Regression Equation")
    print(Border)

    YP = []

    for values in X:
        ret = RegressionEquation(m, values, C)
        YP.append(ret)
        print(f"Predicted Y for X = {values} : {ret}")

    print(Border)
    # YP = m X + C

    # R2 = sum(YP - mean_Y) square / sum(Y - mean_Y) square

    yp_mean_y_squr_sum = 0.0

    for d in YP:
        Ans = (d - mean_Y) ** 2
        yp_mean_y_squr_sum = yp_mean_y_squr_sum + Ans

    print("sum(YP - mean_Y) square : ", yp_mean_y_squr_sum)

    y_mean_y_squr = 0.0
    for d in Y:
        Ans = (d - mean_Y) ** 2
        y_mean_y_squr = y_mean_y_squr + Ans

    print("sum(Y - mean_Y) square : ",y_mean_y_squr)

    R2 = yp_mean_y_squr_sum / y_mean_y_squr

    print("R2 Squared : ", R2)

    y_yp_sum = 0.0
    for i in range(len(Y)):
        Ans = (Y[i] - YP[i]) ** 2
        y_yp_sum = y_yp_sum + Ans

    # MSE = y_yp_sum / Total Y

    MSE = y_yp_sum / len(Y)

    print("Mean Square Error (MSE) : ", MSE)
    
    print(Border)
    
if(__name__ == "__main__"):
    main()