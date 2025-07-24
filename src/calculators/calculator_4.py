from typing import Dict, List
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_data(body)
        mean = self.__calculate_mean(input_data)
        response = self.__format_response(mean)
        return response

    def __validate_data(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body invalid")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_mean(self, numbers: List[float]) -> float:
        mean = self.__driver_handler.mean(numbers)
        return mean
    
    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "mean": round(mean, 2)
            }
        }