'''
Created on 28.01.2022

@author: norbert
'''
from Bruch import Bruch
from Operator import Operator

class Operator_Bruch(object):
    
    __operator: Operator
    __op_1: int
    __op_2: int
    __nenner: int

    def __init__(self, operator: Operator, op_1: int, op_2: int, nenner: int) -> None:
        if nenner == 0:
            raise ZeroDivisionError
        faktor = 1 if (nenner > 0) else -1
        self.__operator = operator
        self.__op_1 = op_1 * faktor
        self.__op_2 = op_2 * faktor
        self.__nenner = nenner * faktor

    @property
    def operator(self) -> Operator:
        return self.__operator
    
    @property
    def op_1(self) -> int:
        return self.__op_1
    
    @property
    def op_2(self) -> int:
        return self.__op_2

    @property
    def nenner(self) -> int:
        return self.__nenner
    
    def berechneBruch(self) -> Bruch:
        return Bruch(self.operator.berechne(self.op_1, self.op_2), self.nenner)