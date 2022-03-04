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


try:
    device_log_object = DeviceLog(
        'D1001', 'Device-X93984', 24, 'Bangalore', '2022-01-01')

    print(device_log_object)
    print('Status : %s' % device_log_object.getStatus())
except Exception as error:
    print('Error Occurred, Details : %s ' % str(error))
