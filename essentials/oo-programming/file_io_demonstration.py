# This Python program is written to parse a device log CSV file using flattened programming style
# STRONGLY NOT RECOMMENDED

import csv
from argparse import ArgumentParser
from os.path import exists

# ArgumentParser is  built-in class which helps to add the support command line arguments to the application
parser = ArgumentParser()
parser.add_argument('-f', '--filename', type=str, required=True,
                    help='Specify Device Log File Name ...')
parser.add_argument('-o', '--outfile', type=str, required=True,
                    help='Specify Device Log Output File Name ...')
parser.add_argument('-s', '--scope', type=str, required=False,
                    help='Specify Device Log Scope Location ...')

# parse_args is a built-in function in ArgumentParser, which processes a given command line argument with keys and values
args = parser.parse_args()

fileName = args.filename
outputFileName = args.outfile
scope = args.scope

print('Output File Name : ' + outputFileName)

if fileName is None or fileName == '':
    fileName = input('Enter the File Name ... ')

if not exists(fileName):
    print('Invalid File Name Specified!')
else:
    print(f'Reading the file {fileName} ...')

    # open is a built-in function, which helps to open a file for reading / writing / appending
    file = open(fileName, mode='r')
    # csv.reader is a built in function that helps to read a CSV file 
    csvFileReader = csv.reader(file)

    # next is a built-in function that helps to skip the current line 
    next(csvFileReader, None) # move to the next line for data reading ...

    for line in csvFileReader:
        deviceLogLocation = line[3]

        if deviceLogLocation == scope:
            print(line)
