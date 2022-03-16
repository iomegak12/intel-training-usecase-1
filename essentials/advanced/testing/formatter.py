def prepare_name(firstName, middleName, lastName):
    if middleName is None:
        middleName = ''

    return f'{lastName}, {firstName} {middleName}'
