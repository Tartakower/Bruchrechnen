from __future__ import annotations
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from Bruch import Bruch
    
from Term_Operand import Term_Operand

class GemischteZahl(Term_Operand):

    def __init__(self, ganzzahl: int, bruch: Bruch) -> None:
        self.__ganzzahl = ganzzahl
        self.__bruch = bruch
        
    @property
    def ganzzahl(self) -> int:
        return self.__ganzzahl
    
    @property
    def bruch(self) -> Bruch:
        return self.__bruch
    
    def __eq__(self, obj: Any) -> bool:
        if isinstance(obj, GemischteZahl):
            return self.ganzzahl == obj.ganzzahl and self.bruch == obj.bruch
        return False
    
    def berechneDezimalzahl(self) -> float:
        return self.ganzzahl + self.bruch.berechneDezimalzahl()
    
    def istGekuerzt(self) -> bool:
        return self.bruch.istEchterBruch() and self.bruch.istGekuerzt()
    
    def berechneBruch(self) -> Bruch:
        from Bruch import Bruch
        return Bruch(self.ganzzahl * self.bruch.nenner + self.bruch.zaehler, self.bruch.nenner)
    
    def kuerze(self) -> GemischteZahl:
        if self.istGekuerzt():
            return self
        return self.berechneBruch().berechneGemischteZahl()        