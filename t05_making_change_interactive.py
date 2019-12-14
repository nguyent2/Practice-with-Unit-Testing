######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Change this to your names
# Username: lovelle & heggens             TODO: Change this to your usernames
#
# Assignment: T05: Unit Testing
#
# Purpose: This file runs the interactive mode of the making change code.
######################################################################
# Acknowledgements:
#
# Original code by: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import t05_making_change         # Notice I'm importing my own code!
                                 # If you see a syntax error here, right click your project folder,
                                 # and select "Mark Directory As..." and select "Sources Root"


def main():
    """
    Runs the interactive mode of the t5_making_change file
    :return: None
    """

    t05_making_change.user_input_of_coins()
    # Notice that the test suite does NOT run here!


main()
