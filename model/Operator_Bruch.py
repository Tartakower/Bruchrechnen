'''
Created on 28.01.2022

@author: norbert
'''
from Grundrechnen import Grundrechnen
from Bruch import Bruch
from Operator import Operator
from Term_Operand import Term_Operand

class Operator_Bruch(Term_Operand):
    
    def __init__(self, operator: Operator, op_1: int, op_2: int, nenner: int) -> None:
        if nenner == 0:
            raise ZeroDivisionError
        faktor = 1 if (nenner > 0) else -1
        self.__zaehler = Grundrechnen(operator, op_1 * faktor, op_2 * faktor)
        self.__nenner = nenner * faktor

    @property
    def zaehler(self) -> Grundrechnen:
        return self.__zaehler

    @property
    def nenner(self) -> int:
        return self.__nenner
    
    def __str__(self):
        return str(self.zaehler) + " / " + str(self.nenner)
    
    def berechneBruch(self) -> Bruch:
        return Bruch(self.zaehler.berechne(), self.nenner)