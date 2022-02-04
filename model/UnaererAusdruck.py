from __future__ import annotations

from typing import Any
from Ausdruck import UnaererAusdruck
from MathUtilities import ggT

""" """
class Bruch(UnaererAusdruck):

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

    def __str__(self) -> str:
        return str(self.zaehler) + " / " + str(self.nenner)

    def __eq__(self, obj: Any) -> bool:
        if isinstance(obj, Bruch):
            return self.zaehler == obj.zaehler and self.nenner == obj.nenner
        return False

    def berechneWert(self) -> float:
        return self.zaehler / self.nenner
    
    def berechneDezimalzahl(self) -> DezimalZahl:
        return DezimalZahl(self.berechneWert())
    
    def istEchterBruch(self) -> bool:
        return self.zaehler < self.nenner
    
    def istGekuerzt(self) -> bool:
        return ggT(self.zaehler, self.nenner) == 1
    
    def kuerze(self) -> Bruch:
        ggt = ggT(self.zaehler, self.nenner)
        return Bruch(self.zaehler // ggt, self.nenner // ggt)
    
    def berechneGemischteZahl(self) -> GemischteZahl:
        b = self.kuerze()
        return GemischteZahl(b.zaehler // b.nenner, Bruch(b.zaehler % b.nenner, b.nenner))

""" """
class GemischteZahl(UnaererAusdruck):

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
        return Bruch(self.ganzzahl * self.bruch.nenner + self.bruch.zaehler, self.bruch.nenner)
    
    def kuerze(self) -> GemischteZahl:
        if self.istGekuerzt():
            return self
        return self.berechneBruch().berechneGemischteZahl()

"""  """
class DezimalZahl(UnaererAusdruck):

    def __init__(self, zahl: float) -> None:
        self.__zahl = zahl

    @property
    def zahl(self) -> float:
        return self.__zahl

    def __str__(self) -> str:
        return str(self.zahl)
    