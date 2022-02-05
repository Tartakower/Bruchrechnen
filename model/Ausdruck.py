"""  """
from __future__ import annotations
from abc import abstractmethod
from typing import List
from Operator import Operator

class Ausdruck(object):

    @abstractmethod
    def berechne(self) -> List[Ausdruck]:
        pass

class UnaererAusdruck(Ausdruck):
    pass

class BinaererAusdruck(Ausdruck):

    def __init__(self, operator: Operator, operand_1: Ausdruck, operand_2: Ausdruck) -> None:
        self.__operator = operator
        self.__operand_1 = operand_1
        self.__operand_2 = operand_2

    @property
    def operator(self) -> Operator:
        return self.__operator

    @property
    def operand_1(self) -> Ausdruck:
        return self.__operand_1

    @property
    def operand_2(self) -> Ausdruck:
        return self.__operand_2

    def __str__(self) -> str:
        return str(self.__operand_1) + " " + str(self.__operator) + " " + str(self.__operand_2)
