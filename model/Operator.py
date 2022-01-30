
from enum import Enum

class Operator(Enum):
    
    PLUS = "+"
    MINUS = "-"
    MULT = "*"
    DIV = "/"

    def __str__(self) -> str:
        return self.value
    
    def berechne(self, a: int, b: int) -> int:
        if (self == Operator.PLUS):
            return a + b
        elif (self == Operator.MINUS):
            return a - b
        elif (self == Operator.MULT):
            return a * b
        elif (self == Operator.DIV):
            return a // b
        else:
            raise ArithmeticError