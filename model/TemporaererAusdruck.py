from __future__ import annotations

from Ausdruck import Ausdruck
from Grundrechnen import Grundrechnen
import MathUtilities
from Operator import Operator
from UnaererAusdruck import Bruch

class TemporaererAusdruck(Ausdruck):
    pass

class SummenBruch(TemporaererAusdruck):
    
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
    
    def __str__(self) -> str:
        return "(" + str(self.zaehler) + "," + str(self.nenner) + ")"
    
    def berechneBruch(self) -> Bruch:
        return Bruch(self.zaehler.berechne(), self.nenner)

class MultBruch(TemporaererAusdruck):
    
    def __init__(self, z_1: int, n_1: int, z_2: int, n_2: int) -> None:
        self.__z1 = z_1
        self.__n1 = n_1
        self.__z2 = z_2
        self.__n2 = n_2
        
    def __str__(self) -> str:
        return "(" + str(Grundrechnen(Operator.MULT, self.__z1, self.__z2)) + "," + str(Grundrechnen(Operator.MULT, self.__n1, self.__n2)) + ")"

    def ist_direkt_gekuerzt(self) -> bool:
        return MathUtilities.ggT(self.__z1, self.__n1) == 1 and MathUtilities.ggT(self.__z2, self.__n2) == 1

    def ist_kreuz_gekuerzt(self) -> bool:
        return MathUtilities.ggT(self.__z1, self.__n2) == 1 and MathUtilities.ggT(self.__z2, self.__n1) == 1
    
    def direkt_kuerzen(self) -> MultBruch:
        ggt_1 = MathUtilities.ggT(self.__z1, self.__n1)
        ggt_2 = MathUtilities.ggT(self.__z2, self.__n2)
        return MultBruch(self.__z1 // ggt_1, self.__n1 // ggt_1, self.__z2 // ggt_2, self.__n2 // ggt_2)
    
    def kreuz_kuerzen(self) -> MultBruch:
        ggt_1 = MathUtilities.ggT(self.__z1, self.__n2)
        ggt_2 = MathUtilities.ggT(self.__z2, self.__n1)
        return MultBruch(self.__z1 // ggt_1, self.__n1 // ggt_2, self.__z2 // ggt_2, self.__n2 // ggt_1)
    

    def berechneBruch(self) -> Bruch:
        return Bruch(self.__z1 * self.__z2, self.__n1 * self.__n2)

    @staticmethod
    def erzeugeErweiterung(bruch: Bruch) -> MultBruch:
        faktor: int = MathUtilities.ggT(bruch.zaehler, bruch.nenner)
        return MultBruch(bruch.zaehler // faktor, bruch.nenner // faktor, faktor, faktor)

    @staticmethod
    def erzeugeMultBruch(bruch_1: Bruch, bruch_2: Bruch) -> MultBruch:
        return MultBruch(bruch_1.zaehler, bruch_1.nenner, bruch_2.zaehler, bruch_2.nenner)