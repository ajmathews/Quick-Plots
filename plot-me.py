# import sys
import matplotlib.pyplot as pl
import numpy as np

def plot_me(x_vals, y_vals, diff_list):
    """Plots the X, Y & diff_list, Y coordinates"""
    pl.plot(np.array(x_vals), np.array(y_vals))
    pl.plot(np.array(x_vals), np.array(diff_list))
    pl.legend(['X vs. Y Plot', '(Y-X) Diff Plot'])
    pl.grid(True)
    pl.show()

def main():
    """Main function"""
    input_choice = 1

    while input_choice:
        print("Welcome to the plotter")
        print("(1) Plot Celsius vs Farenheit")
        print("(2) Plot Kilometers vs Miles")
        print("(3) Plot Kilograms vs Pounds")
        print("(M) Manually give the X and Y lists")
        print("(0) Exit")
        print("")

        input_choice = input("Please enter your choice: ")

        y = list()

        if input_choice == '1':

            print("You entered Choice 1")
            x = range(-30, 30, 1)
            for val in x:
                y.append((val*9)/5 + 32)

            pl.xlabel("Celsius")
            pl.ylabel("Farenheit")

        elif input_choice == '2':

            print("You entered Choice 2")
            x = range(0, 140, 1)
            for val in x:
                y.append(val*0.621371)
            pl.xlabel("Kilometers")
            pl.ylabel("Miles")

        elif input_choice == '3':

            print("You entered Choice 3")
            x = range(0, 100, 1)
            for val in x:
                y.append(val*2.20462)
            pl.xlabel("Kilograms")
            pl.ylabel("Pounds")

        elif input_choice == 'M':

            print("You entered Choice 3")
            x = input("Enter the X values [1,2,3,..]:")
            y = input("Enter the Y values [1,2,3,..]:")

        else:
            print("Bye Bye!!")
            exit()

        # Finding the average difference
        sum_of_diffs = 0
        difference_list = list()
        for val, val2 in zip(x, y):
            sum_of_diffs = sum_of_diffs + abs(val - val2)
            difference_list.append(abs(val - val2))

        average_diff = sum_of_diffs/len(x)
        print("The average difference is ", average_diff)
        plot_me(x, y, difference_list)

if __name__ == "__main__":
    # main(sys.argv)
    main()
