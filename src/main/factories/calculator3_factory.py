from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3


def calculator3_factory():
    numpy_handler = NumpyHandler()
    return Calculator3(driver_handler=numpy_handler)
