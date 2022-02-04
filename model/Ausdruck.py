"""  """

from Operator import Operator


class Ausdruck(object):
    pass

class UnaererAusdruck(Ausdruck):
    pass

class BinaererAusdruck(Ausdruck):

    def __init__(self, operator: Operator, operand_1: UnaererAusdruck, operand_2: UnaererAusdruck) -> None:
        self.__operator = operator
        self.__operand_1 = operand_1
        self.__operand_2 = operand_2

    @property
    def operator(self) -> Operator:
        return self.__operator

    @property
    def operand_1(self) -> UnaererAusdruck:
        return self.__operand_1

    @property
    def operand_2(self) -> UnaererAusdruck:
        return self.__operand_2

    def __str__(self) -> str:
        return str(self.__operand_1) + " " + str(self.__operator) + " " + str(self.__operand_2)