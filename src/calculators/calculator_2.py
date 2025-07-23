from typing import Dict, List
from flask import Request
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
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
        numpy_handler = NumpyHandler()
        first_process_result = [(x * 11) ** 0.95 for x in input_data]
        result = numpy_handler.standard_derivation(first_process_result)
        return 1 / result
    
    def __format_response(self, calc_result: float) -> Dict:
        return {"data": {"Calculator": 2, "result": round(calc_result, 2)}}