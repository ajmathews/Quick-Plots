import matplotlib.pyplot as pl
import numpy as np

def PlotMe(x, y, diffList):
    print(y)
    pl.plot(np.array(x), np.array(y))
    pl.plot(np.array(x), np.array(diffList))
    pl.legend(['X vs. Y Plot', '(Y-X) Diff Plot'])
    pl.grid(True)
    pl.show()

choice = 1

while choice:
    print("Welcome to the plotter")
    print("(1) Plot Celsius vs Farenheit")
    print("(2) Plot Kilometers vs Miles")
    print("(3) Manually give the X and Y lists")
    print("(0) Exit")
    print("")

    choice = input("Please enter your choice: ")

    y = list()

    if choice == '1':

        print("You entered Choice 1")
        x = range(-30, 30, 1)
        for val in x:
            y.append((val*9)/5 + 32)

        pl.xlabel("Celsius")
        pl.ylabel("Farenheit")

    elif choice == '2':

        print("You entered Choice 2")
        x = range(0, 140, 1)
        for val in x:
            y.append(val*0.621371)
        pl.xlabel("Kilometers")
        pl.ylabel("Miles")

    elif choice == '3':

        print("You entered Choice 3")
        x = input("Enter the X values [1,2,3,..]:")
        y = input("Enter the Y values [1,2,3,..]:")

    else:
        exit()

    # Finding the average difference
    sumOfDiffs = 0
    diffList = list()
    for val,val2 in zip(x, y):
        sumOfDiffs = sumOfDiffs + abs(val - val2)
        diffList.append(abs(val - val2))

    avg = sumOfDiffs/len(x)
    print("The average difference is ", avg)
    PlotMe(x, y, diffList)
