from os.path import exists
import csv
import threading

def parse_logs(logFileName, callback):
    if logFileName is None or not exists(logFileName):
        raise Exception('Invalid File Name Specified!')

    with open(logFileName, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the header

        logs = []

        for line in reader:
            deviceId = line[0]
            deviceName = line[1]
            temperature = int(line[2])
            location = line[3]
            recordDate = line[4]

            log = (deviceId, deviceName, temperature, location, recordDate)
            logs.append(log)

        if callback is not None:
            callback(logs)

if __name__ == "__main__":
    logFileName = './device_logs.log'
    callback = lambda logEntries: [print(log) for log in logEntries]
    parserThread = threading.Thread(
        target = parse_logs, args = (logFileName, callback))

    parserThread.start()

    print('Continuing to execute other main instructions ...')

    parserThread.join()

    print(f'Thread Status : {parserThread.is_alive()}')
    print('End of the Application!')