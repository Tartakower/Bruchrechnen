from __future__ import annotations
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from GemischteZahl import GemischteZahl
     
from MathUtilities import ggT    
from Term_Operand import Term_Operand

class Bruch(Term_Operand):

    def __init__(self, zaehler: int, nenner: int) -> None:
        if nenner == 0:
            raise ZeroDivisionError
        faktor = 1 if (nenner > 0) else -1
        self.__zaehler = zaehler * faktor
        self.__nenner = nenner * faktor

    @property
    def zaehler(self) -> int:
        return self.__zaehler

    @property
    def nenner(self) -> int:
        return self.__nenner

    def __eq__(self, obj: Any) -> bool:
        if isinstance(obj, Bruch):
            return self.zaehler == obj.zaehler and self.nenner == obj.nenner
        return False

    def berechneDezimalzahl(self) -> float:
        return self.zaehler / self.nenner
    
    def istEchterBruch(self) -> bool:
        return self.zaehler < self.nenner
    
    def istGekuerzt(self) -> bool:
        return ggT(self.zaehler, self.nenner) == 1
    
    def kuerze(self) -> Bruch:
        ggt = ggT(self.zaehler, self.nenner)
        return Bruch(self.zaehler // ggt, self.nenner // ggt)
    
    def berechneGemischteZahl(self) -> GemischteZahl:
        b = self.kuerze()
        from GemischteZahl import GemischteZahl
        return GemischteZahl(b.zaehler // b.nenner, Bruch(b.zaehler % b.nenner, b.nenner))