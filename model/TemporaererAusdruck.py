from __future__ import annotations

from Ausdruck import Ausdruck
from Grundrechnen import Grundrechnen
import MathUtilities
from Operator import Operator
from UnaererAusdruck import Bruch

class TemporaererAusdruck(Ausdruck):
    pass

class AdditionBruch(TemporaererAusdruck):
    
    def __init__(self, op_1: int, op_2: int, nenner: int) -> None:
        if nenner == 0:
            raise ZeroDivisionError
        faktor = 1 if (nenner > 0) else -1
        self.__zaehler = Grundrechnen(Operator.PLUS, op_1 * faktor, op_2 * faktor)
        self.__nenner = nenner * faktor

    @property
    def zaehler(self) -> Grundrechnen:
        return self.__zaehler

    @property
    def nenner(self) -> int:
        return self.__nenner
    
    def __str__(self) -> str:
        return str(self.zaehler) + " / " + str(self.nenner)
    
    def berechneBruch(self) -> Bruch:
        return Bruch(self.zaehler.berechne(), self.nenner)

class MultBruch(TemporaererAusdruck):
    
    def __init__(self, z_1: int, n_1: int, z_2: int, n_2: int) -> None:
        self.__zaehler = Grundrechnen(Operator.MULT, z_1, z_2)
        self.__nenner = Grundrechnen(Operator.MULT, n_1, n_2)
        
    @property
    def zaehler(self) -> Grundrechnen:
        return self.__zaehler

    @property
    def nenner(self) -> Grundrechnen:
        return self.__nenner
    
    def __str__(self) -> str:
        return str(self.zaehler) + " / " + str(self.nenner)
    
    def direkt_kuerzen(self) -> MultBruch:
        ggt = MathUtilities.ggT(self.zaehler.operand_1, self.nenner.operand_1)
        z_1 = self.zaehler.operand_1 // ggt
        n_1 = self.nenner.operand_1 // ggt
        ggt = MathUtilities.ggT(self.zaehler.operand_2, self.nenner.operand_2)
        z_2 = self.zaehler.operand_2 // ggt
        n_2 = self.nenner.operand_2 // ggt
        return MultBruch(z_1, n_1, z_2, n_2)
    
    def kreuz_kuerzen(self) -> MultBruch:
        ggt = MathUtilities.ggT(self.zaehler.operand_1, self.nenner.operand_2)
        z_1 = self.zaehler.operand_1 // ggt
        n_2 = self.nenner.operand_2 // ggt
        ggt = MathUtilities.ggT(self.zaehler.operand_2, self.nenner.operand_1)
        z_2 = self.zaehler.operand_2 // ggt
        n_1 = self.nenner.operand_1 // ggt
        return MultBruch(z_1, n_1, z_2, n_2)
    

    def berechneBruch(self) -> Bruch:
        return Bruch(self.zaehler.berechne(), self.nenner.berechne())