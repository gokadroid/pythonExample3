import json
import getopt, sys
from pathlib import Path
import sys
import time
import datetime


"""
 Function to take the -j or --json option for json filepath name
"""

def menu():
    #accept the commandline arguments into a variable
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]
    # provide the gnu and unix options of how argument will be taken at command line.
    # Below options will take -j or --json as valid argument followed by the file Name (say)
    unixOptions = "j:"
    gnuOptions = ["json="]
    """
    #you can also give multiple options like below
    #nixOptions = "ho:"  
    #gnuOptions = ["help", "output="]  
    """

    try:
        #if all succeeds till here return the arguments and the values from inbuilt getopt function
        return getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
        print ("Usage: python "+sys.argv[0]+" "+"[-j | --json ] [ absolutePathOfJsonConfigFile ]")
        sys.exit(2)
    return

#call the menu function and save the arguments returned from it
arguments, values= menu()
if len(arguments) < 1:
    print ("Usage: python "+sys.argv[0]+" "+"[-j | --json ] [ absolutePathOfJsonConfigFile ]")
    sys.exit(3)
for argumentSupplied, valueSupplied in arguments:
    #cate for your options (-j or --json in this case)
    if argumentSupplied in ("-j", "--json"):
        #use the value after the -j or --json via valueSupplied
        my_json_file = Path(valueSupplied)
        if my_json_file.exists():
            print("I can use the json file here and do whatever is needed")
        else:
            #seems like json file path provided doesnt exist
            print("File "+valueSupplied+" doesnt exist!!")
            sys.exit(3)
