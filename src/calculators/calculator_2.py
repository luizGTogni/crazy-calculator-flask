from typing import Dict, List
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        calc_result = self.__process_data(input_data)
        response = self.__format_response(calc_result)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body invalid")
        
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(x * 11) ** 0.95 for x in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)
        return 1 / result
    
    def __format_response(self, calc_result: float) -> Dict:
        return {"data": {"Calculator": 2, "result": round(calc_result, 2)}}