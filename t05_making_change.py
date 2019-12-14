######################################################################
# Author: Thy H. Nguyen and Jennifer Fidelia          TODO: Change this to your names
# Username: nguyent2 and fideliaj             TODO: Change this to your usernames
#
# Assignment: T05: Unit Testing
#
# Purpose: Demonstrates the use of division and modulus operations.
#
# This program INCORRECTLY calculates the largest number of
# quarters, dimes, nickels and pennies needed to make that change in coins.
# It is designed to show a subtle error and the value of unit tests.
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys


def testit(did_pass):
    """
    Print the result of a unit test.
    This function works correctly--it is verbatim from the textbook, Chapter 6.
    You should reuse this function anytime you are creating a custom test suite
    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def pennies_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the is_i_steal_pennies() function,
    returning True only when the input is even.
    :return: None
    """
    print("\nRunning pennies_testsuite()).")

    # Remember that I_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    testit(i_steal_pennies(0.88) == [3, 1, 0, 3]) # because three quarters, 1 dime, and 3 pennies equals 88 cents
    testit(i_steal_pennies(0.89) == [3, 1, 0, 4]) # because three quarters, 1 dime, and 4 pennies equals 89 cents
    testit(i_steal_pennies(0) == [0,0,0,0]) # because 0 quarters, 0 dime, 0 nickels, and 0 pennies equals 0
    testit(i_steal_pennies(0.01) == [0,0,0,1]) #because 0 quarters, 0 dime, 0 nickels, and 1 pennies equals 0.01
    testit(i_steal_pennies(4000)== [16000,0,0,0]) #because 0 quarters, 0 dime, 0 nickels, and 0 pennies equals 0
    #testit(i_steal_pennies($4000)== [1600,0,0,0])
    testit(i_steal_pennies(2) == [8,0,0,0])
    testit(i_steal_pennies(0.00001) == [0,0,0,0])
    testit(i_steal_pennies(2.000000001) == [8,0,0,0])
    testit(i_steal_pennies(1000000)==[4000000,0,0,0])
    testit(i_steal_pennies(4000002.88 == []))
    testit(i_steal_pennies(13)==[52,0,0,0])
    testit(i_steal_pennies(73)==[292,0,0,0])
    testit(i_steal_pennies(2.01)==[8,0,0,1])
    testit(i_steal_pennies(2.51)==[10,0,0,1])
    testit(i_steal_pennies(2.76) ==[11,0,0,1])
    testit(i_steal_pennies(2.56)==[10,0,1,1])
    testit(i_steal_pennies(0.01)==[0,0,0,1])
    testit(i_steal_pennies(2.77)==[11,0,0,2])
    a=(float(2.76%0.25))
    b=float(2.51%0.25)
    print(b)
    print(a)
    print(a>=0.01)
    print(int(a/0.01))
    # TODO ADD MORE UNIT TESTS HERE!


    print("Run of pennies_testsuite() complete.")


def i_steal_pennies(to_change):
    """
    This function looks like it should take a floating point number to_change
    and return a list of how much change to give as [num_quarters, num_dimes, num_nickels, num_pennies]
    However, it compounds small truncation errors of the floating point arithmetic.
    Such errors are subtle and can be quite hard to debug, so unit tests are useful!
    A better algorithm would be to use integers instead of floats,
    but the point of this assignment is NOT to fix the error.
    It IS to help you learn to use and to value unit tests.
    :param to_change: a float representing an amount of money
    :return: A list of the number of quarters, dimes, nickels,
             and pennies representing the amount of money above
    """
    # TODO DO NOT CHANGE THIS FUNCTION!

    # Initialize values
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    # Compute numbers of each coin type
    if to_change >= 0.25:
        num_quarters = int(to_change / 0.25)
        to_change = float(to_change % 0.25)

    if to_change >= 0.1:
        num_dimes = int(to_change / 0.1)
        to_change = float(to_change % 0.1)

    if to_change >= 0.05:
        num_nickels = int(to_change / 0.05)
        to_change = float(to_change % 0.05)

    if to_change >= 0.01:
        num_pennies = int(to_change / 0.01)

    return [num_quarters, num_dimes, num_nickels, num_pennies] # this order will be retained


def print_change(coinlist):
    """
    This program expects an input coin list of [num_quarters, num_dimes, num_nickels, num_pennies]
    It will print the values out for the user.
    :param coinlist: A list of the number of quarters, dimes, nickels,
                     and pennies representing the amount of money above
    :return: None
    """

    print("Can you tell if I am an honest machine? ")
    print("Give out the following change: ")
    valuelist = ["Quarter(s): ", "Dime(s): ", "Nickel(s): ", "Penny(s): "]
    for item in range(4):
        print(valuelist[item] + str(coinlist[item]))


def user_input_of_coins():
    """
    This function is created just for interactive fun.
    This would be for the normal mode of operation (not testing)
    :return: None
    """

    the_total = float(input("Input total amount of dollars and cents (e.g., 2.45): "))
    print("You have asked how to make " + str(the_total)+ " in change.")
    list_of_change = i_steal_pennies(the_total)
    print_change(list_of_change)


def main():
    """
    This main function is intended to test the correctness of the i_steal_pennies() function
    :return:
    """

    pennies_testsuite()


if __name__ == "__main__":
    # If you run this code directly (i.e., hit the green run button on this file), it runs the test suite
    # If you call this code from another file (e.g., t05_making_change_interactive.py), it will NOT run the test suite
    main()
