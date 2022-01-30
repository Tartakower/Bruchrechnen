
from Operator import Operator

class Grundrechnen():
    
    def __init__(self, oper: Operator, op_1: int, op_2: int) -> None:
        self.__operator = oper
        self.__operand_1 = op_1
        self.__operand_2 = op_2
        
    @property
    def operator(self) -> Operator:
        return self.__operator
    
    @property
    def operand_1(self) -> int:
        return self.__operand_1
    
    @property
    def operand_2(self) -> int:
        return self.__operand_2
    
    def __str__(self)-> str:
        return str(self.operand_1) + " " + str(self.operator) + " " + str(self.operand_2)
    
    def berechne(self) -> int:
        return self.operator.berechne(self.operand_1, self.operand_2)
    
    def mathML(self) -> str:
        return "<mn>" + str(self.operand_1) + "</mn><mo>" + str(self.operator) + "</mo><mn>" + str(self.operand_2) + "</mn>"