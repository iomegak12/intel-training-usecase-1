# This Python program is written to parse a device log CSV file using procedured / structured programming style
# RECOMMENDED

import csv
from argparse import ArgumentParser


class DeviceLog:
    def __init__(self, deviceId, deviceName, temperature, location, recordDate):
        self.deviceId = deviceId
        self.deviceName = deviceName
        self.temperature = temperature
        self.location = location
        self.recordDate = recordDate

    def getStatus(self):
        if self.temperature is None:
            raise Exception('Invalid Temperature Value Specified!')

        if self.temperature < 18:
            status = 'COLD'
        elif self.temperature >= 18 and self.temperature < 25:
            status = 'WARM'
        else:
            status = 'HOT'

        return status

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.deviceId, self.deviceName,
                                       self.temperature, self.location, self.recordDate)


def parseLogs(fileName):
    file = open(fileName, mode='r')
    csvFileReader = csv.reader(file)
    next(csvFileReader, None)
    deviceLogs = []

    for line in csvFileReader:
        deviceId = line[0]
        deviceName = line[1]
        temperature = int(line[2])
        location = line[3]
        recordDate = line[4]

        deviceLog = DeviceLog(deviceId, deviceName,
                              temperature, location, recordDate)
        deviceLogs.append(deviceLog)

    return deviceLogs


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, required=True,
                        help='Specify Device Log File Name ...')

    args = parser.parse_args()
    inputFileName = args.filename
    parsedDeviceLogs = parseLogs(inputFileName)
    usLocations = ['New York', 'Seattle', 'Houston']

    for log in parsedDeviceLogs:
        if log.location in usLocations:
            print(log)


if __name__ == '__main__':
    main()
