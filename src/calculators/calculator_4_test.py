from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def mean(self, numbers: List[float]) -> float:
        total = 0
        for n in numbers:
            total += n

        return total / len(numbers)

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": [5]})
    calc = Calculator4(driver_handler=MockDriverHandler)

    with raises(Exception) as excinfo:
        response = calc.calculate(mock_request)

    assert str(excinfo.value) == "body invalid"


def test_calculate():
    mock_request = MockRequest(body={"numbers": [5, 4, 8, 4, 5]})
    calc = Calculator4(driver_handler=MockDriverHandler())
    response = calc.calculate(mock_request)
    print(response)

    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 4, 'mean': 5.2}}