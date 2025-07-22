from typing import Dict
from flask import Request

class Calculator1:
    '''
    * Um número é dividido em 3 partes iguais.

    * A primeira parte é dividida por 4 e seu resultado somado a 7.
    Após isso, o resultado é elevado ao quadrado e multiplicado por um valor de 0.257.
    '''

    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body invalid")
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7 
        second_part = (first_part ** 2) * 0.257
        return second_part