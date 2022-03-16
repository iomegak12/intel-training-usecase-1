import formatter
import os
import pytest

def test_formatter_method():
    # expectedResult = os.environ.get('EXPECTED_RESULT')

    expectedResult = "Damodaran, Ramkumar J"
    firstName = 'Ramkumar'
    middleName = 'J'
    lastName = 'Damodaran'

    actualResult = formatter.prepare_name(firstName, middleName, lastName)

    assert actualResult == expectedResult, "Formatter Test Failed!"
