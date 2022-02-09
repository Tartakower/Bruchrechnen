"""  """

from typing import cast
from Ausdruck import BinaererAusdruck
from Operator import Operator
from UnaererAusdruck import Bruch

class BinaererBruchAusdruck(BinaererAusdruck):

    def __init__(self, operator: Operator, operand_1: Bruch, operand_2: Bruch) -> None:
        super().__init__(operator, operand_1, operand_2)

    def getOperand_1(self) -> Bruch:
        return cast(Bruch, self.operand_1)

    def getOperand_2(self) -> Bruch:
        return cast(Bruch, self.operand_2)

class Summe(BinaererBruchAusdruck):    
    
    def __init__(self, operator: Operator, summand_1: Bruch, summand_2: Bruch) -> None:
        super().__init__(operator, summand_1, summand_2)

class Multiplikation(BinaererBruchAusdruck):

    def __init__(self, faktor_1: Bruch, faktor_2: Bruch) -> None:
        super().__init__(Operator.MULT, faktor_1, faktor_2)

class Division(BinaererBruchAusdruck):

    def __init__(self, faktor_1: Bruch, faktor_2: Bruch) -> None:
        super().__init__(Operator.DIV, faktor_1, faktor_2)