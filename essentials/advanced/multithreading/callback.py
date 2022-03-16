from time import sleep


def load_data(callback):
    print('Started ... ')
    sleep(3)
    print('Loading Completed ...')

    if callback is not None:
        result = 10
        callback(result)


def handle_result(result):
    print(f'Result is : {result}')


# load_data(callback=handle_result)
load_data(callback = lambda result: print(f'Result is : {result}'))

print('This statement shall not be executed until load_data() completes ...')
