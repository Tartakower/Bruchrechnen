from __future__ import annotations
from MathUtilities import ggT

class Bruch(object):

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

    def berechneDezimalzahl(self) -> float:
        return self.zaehler / self.nenner
    
    def kuerze(self) -> Bruch:
        ggt = ggT(self.zaehler, self.nenner)
        return Bruch(self.zaehler // ggt, self.nenner // ggt)
        