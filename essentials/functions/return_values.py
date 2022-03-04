def absolute_value(num: int):
    """
        This function returns the absoluate value of the provided number
    """

    if num >= 0:
        return num
    
    return -num

result = absolute_value(-100)

print('Processed Result : ' + str(result))

