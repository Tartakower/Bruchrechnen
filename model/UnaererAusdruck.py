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
        return "(" + str(self.zaehler) + "," + str(self.nenner) + ")"

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

    def kehrwert(self) -> Bruch:
        return Bruch(self.nenner, self.zaehler)
    
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

    def __str__(self) -> str:
        return str(self.ganzzahl) + " " + str(self.bruch)
    
    def berechneBruch(self) -> Bruch:
        return Bruch(self.ganzzahl * self.bruch.nenner + self.bruch.zaehler, self.bruch.nenner)

    def berechneDezimalzahl(self) -> DezimalZahl:
        return DezimalZahl(self.ganzzahl + self.bruch.berechneWert())

    def istEcht(self) -> bool:
        return self.bruch.istEchterBruch()
    
    def istGekuerzt(self) -> bool:
        return self.bruch.istGekuerzt()
    
    def istNormiert(self) -> bool:
        return self.istEcht() and self.istGekuerzt()

    def extrahiereGanzzahl(self) -> GemischteZahl:
        if self.istEcht():
            return self
        zaehler: int = self.bruch.zaehler
        nenner: int = self.bruch.nenner
        return GemischteZahl(self.ganzzahl + zaehler // nenner, Bruch(zaehler % nenner, nenner))

    def kuerze(self) -> GemischteZahl:
        if self.istGekuerzt():
            return self
        return self.berechneBruch().berechneGemischteZahl()

    def normiere(self) -> GemischteZahl:
        normierteZahl = self
        if not self.istEcht():
            normierteZahl = self.extrahiereGanzzahl()
        if not normierteZahl.istGekuerzt():
            normierteZahl = normierteZahl.kuerze()
        return normierteZahl

"""  """
class DezimalZahl(UnaererAusdruck):

    def __init__(self, zahl: float) -> None:
        self.__zahl = zahl

    @property
    def zahl(self) -> float:
        return self.__zahl

    def __str__(self) -> str:
        return str(self.zahl)

    def berechneBruch(self, gekuerzt: bool) -> Bruch:
        nachkommastellen: str = str(self.zahl).partition(".")[2]
        anzahl: int = len(nachkommastellen)
        nenner: int = pow(10,anzahl)
        bruch: Bruch = Bruch(int(self.zahl * nenner), nenner)
        return bruch.kuerze() if gekuerzt else bruch

    def berechneGemischteZahl(self) -> GemischteZahl:
        return self.berechneBruch(True).berechneGemischteZahl()    