class Employee:
    def __init__(self, employeeId, name, jobTitle):
        self.employeeId = employeeId
        self.name = name
        self.jobTitle = jobTitle

    def work(self, taskName, taskDescription='',  **taskProperties):
        if taskName is None:
            print('Sorry, I may not be able to work without task name ...')
            raise Exception('Task Name is Not Valid!')

        print(f'{taskName} - Started ...')
        print(f'{taskDescription} ...')

        for propertyName, propertyValue in taskProperties.items():
            print(f'{propertyName} - {propertyValue}')

        print('Task Completed ...')


try:
    pattinson = Employee('E10001', 'Robert Pattinson', 'Actor')

    pattinson.work("The Batman", 'Casting as a Batman Character',
                   detective_type='Luxury',
                   detective_time='Nightcrawler',
                   vehicle_type='Batcar')
except Exception as error:
    print(f'Sorry, Error Occurred, Details, {str(error)}')
finally:
    print('End of the World!')
