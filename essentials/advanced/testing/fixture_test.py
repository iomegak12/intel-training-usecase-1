import pytest
import formatter


@pytest.fixture
def supply_test_values():
    firstName = 'Ramkumar'
    middleName = 'J'
    lastName = 'Damodaran'

    return [firstName, middleName, lastName]

@pytest.mark.xfail
def test_method1(supply_test_values):
    firstName, middleName, lastName = supply_test_values

    expectedResult = 'Damodaran, Ramkumar JK'
    actualResult = formatter.prepare_name(firstName, middleName, lastName)

    assert actualResult == expectedResult, "Prepare Name Test Failed!"
