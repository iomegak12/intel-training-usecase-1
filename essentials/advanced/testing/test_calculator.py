import pytest
import calculator


def test_add_method():
    inputA = 10
    inputB = 20

    actualResult = calculator.add(inputA, inputB)
    expectedResult = 30

    assert actualResult == expectedResult, "Test Failed"
