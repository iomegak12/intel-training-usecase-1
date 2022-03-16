import argparse
from jinja2 import Template
from os.path import exists
import json


def main(templateFileName, dataFileName, outputFileName):
    validation = templateFileName is not None and exists(templateFileName) and \
        dataFileName is not None and exists(dataFileName)

    if not validation:
        print('Invalid Template or Data File Name Specified!')
        exit()

    with open(templateFileName, mode='r', encoding='utf-8') as templateFile:
        with open(dataFileName, mode='r', encoding='utf-8') as dataFile:
            templateFileContents = templateFile.readlines()
            dataFileContents = dataFile.readlines()
            templateContents = "".join(templateFileContents)
            dataContents = "".join(dataFileContents)

            data = json.loads(dataContents)
            inputTemplate = Template(templateContents)
            processedOutput = inputTemplate.render(data)

            with open(outputFileName, mode='w', encoding='utf-8') as outputFile:
                outputFile.write(processedOutput)

    print('End of the Application!')


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--inputfilename", required=True, type=str)
parser.add_argument("-d", "--datafilename", required=True, type=str)
parser.add_argument("-o", "--outputfilename", required=True, type=str)

args = parser.parse_args()

main(templateFileName=args.inputfilename,
     dataFileName=args.datafilename,
     outputFileName=args.outputfilename)
