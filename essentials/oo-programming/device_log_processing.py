import csv
from os.path import exists
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


class DeviceLogFileParser:
    def __init__(self, deviceLogFile):
        validation = deviceLogFile is not None and exists(deviceLogFile)

        if not validation:
            raise Exception('Invalid Device Log Input File Name Specified!')

        self.deviceLogFile = deviceLogFile

    def parseLogs(self):
        deviceLogs = []
        try:
            file = open(self.deviceLogFile, mode='r')
            csvReader = csv.reader(file)
            next(csvReader, None)  # skip the header

            for line in csvReader:
                deviceId, deviceName, temperature, location, recordDate = line
                deviceLog = DeviceLog(
                    deviceId, deviceName, temperature, location, recordDate)
                deviceLogs.append(deviceLog)
        except Exception as error:
            print('Unable to Process Device Log Input File ... %s' % str(error))
        finally:
            file.close()

        return deviceLogs


def main():
    try:
        parser = ArgumentParser()
        parser.add_argument('-f', '--filename', type=str, required=True,
                            help='Specify Device Log File Name ...')

        args = parser.parse_args()

        inputFileName = args.filename
        deviceLogFileParser = DeviceLogFileParser(inputFileName)
        deviceLogs = deviceLogFileParser.parseLogs()
        usLocations = ["New York", "Houston", "Seattle"]
        usDeviceLogs = [
            log for log in deviceLogs if log.location in usLocations]

        for usDeviceLog in usDeviceLogs:
            print(usDeviceLog)
    except Exception as error:
        print('Error Occurred, Details : %s' % str(error))


if __name__ == '__main__':
    main()
