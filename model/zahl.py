from __future__ import annotations
import matheHelfer

class Zahl():
    pass


class Bruch(Zahl):
    
    def __init__(self, zaehler: int, nenner: int):
        self.__zaehler = zaehler
        self.__nenner = nenner

    def __str__(self: Bruch) -> str:
        return str(self.zaehler) + "/" + str(self.nenner)

    @property
    def zaehler(self: Bruch) -> int:
        return self.__zaehler

    @property
    def nenner(self: Bruch) -> int:
        return self.__nenner
        
    def berechneWert(self: Bruch) -> float:
        return self.zaehler / self.nenner

    def kuerze(self: Bruch) -> Bruch:
        alterZaehler = self.zaehler
        alterNenner = self.nenner
        kuerzungsFaktor = matheHelfer.ggT(alterZaehler, alterNenner)
        neuerZaehler = alterZaehler // kuerzungsFaktor
        neuerNenner = alterNenner // kuerzungsFaktor
        neuerBruch = Bruch(neuerZaehler, neuerNenner)
        return neuerBruch

    def berechneDezimalzahl(self: Bruch) -> Dezimalzahl:
        wert = self.berechneWert()
        return Dezimalzahl(wert)

class Dezimalzahl():

    def __init__(self: Dezimalzahl, zahl: float):
        self.__zahl = zahl

    def __str__(self: Dezimalzahl) -> str:
        return str(self.zahl)

    @property
    def zahl(self: Dezimalzahl) -> float:
        return self.__zahl

    def berechneWert(self: Dezimalzahl) -> float:
        return self.zahl

    def berechneBruch(self: Dezimalzahl) -> Bruch:
        dezimalwert = self.zahl
        zahlAlsString = str(dezimalwert)
        nachkommastellen: str = zahlAlsString.partition(".")[2]
        anzahlNachkommastellen = len(nachkommastellen)
        neuerNenner = pow(10,anzahlNachkommastellen)
        neuerZaehler = int(dezimalwert * neuerNenner)
        neuerBruch = Bruch(neuerZaehler, neuerNenner)
        return neuerBruch