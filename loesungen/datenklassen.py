from __future__ import annotations
from abc import abstractmethod
from dataclasses import dataclass
import mathefunktionen

class Zahl():

    @abstractmethod
    def berechneBruch(self) -> Bruch:
        pass

@dataclass(frozen=True)
class Bruch(Zahl):

    zaehler: int
    nenner: int

    def berechneBruch(self) -> Bruch:
        return self

    def kuerze(self) -> Bruch:
        ggT = mathefunktionen.berechne_ggT(self.zaehler, self.nenner)
        return Bruch(self.zaehler // ggT, self.nenner // ggT)

    def erweitere(self, faktor: int) -> Bruch:
        return Bruch(faktor * self.zaehler, faktor * self.nenner)

    def berechneAdditivInverses(self) -> Bruch:
        return Bruch(-1 * self.zaehler, self.nenner)

    def berechneKehrwert(self) -> Bruch:
        return Bruch(self.nenner, self.nenner)

    def berechneDezimalzahl(self) -> Dezimalzahl:
        return Dezimalzahl(self.zaehler / self.nenner)

@dataclass(frozen=True)
class Dezimalzahl(Zahl):

    kommazahl: float

    def berechneBruch(self) -> Bruch:
        nenner = mathefunktionen.berechne_ZehnerPotenz(self.kommazahl)
        zaehler = int(self.kommazahl * nenner)
        return Bruch(zaehler, nenner).kuerze()

@dataclass(frozen=True)
class GemischteZahl(Zahl):

    ganzzahl: int
    bruch: Bruch

    def berechneBruch(self) -> Bruch:
        return Bruch(self.ganzzahl * self.bruch.nenner + self.bruch.zaehler, self.bruch.nenner).kuerze()

    def normiere(self) -> GemischteZahl:
        gz = self.bruch.zaehler // self.bruch.nenner
        bruch = Bruch(self.bruch.zaehler - gz * self.bruch.nenner, self.bruch.nenner)
        return GemischteZahl(gz, bruch)

# Funktionen für MathML

def schreibeBruch(bruch: Bruch) -> str:
    zaehlerAlsString = str(bruch.zaehler)
    nennerAlsString = str(bruch.nenner)
    ergebnis = "<mfrac>"
    ergebnis = ergebnis + "<mn>" + zaehlerAlsString + "</mn>"
    ergebnis = ergebnis + "<mn>" + nennerAlsString + "</mn>"
    ergebnis = ergebnis + "</mfrac>"
    return ergebnis

def schreibeDezimalzahl(dezimalzahl: Dezimalzahl) -> str:
    dezimalwert = dezimalzahl.kommazahl
    zahlAlsString = str(dezimalwert)
    ergebnis = "<mn>" + zahlAlsString + "</mn>"
    return ergebnis

def schreibeErweitern(bruch: Bruch, faktor: int) -> str:
    bruchErweitert = bruch.erweitere(faktor)
    textAlterBruch = schreibeBruch(bruch)
    textNeuerBruch = schreibeBruch(bruchErweitert)
    ergebnis = textAlterBruch + "<mo>=</mo>" + textNeuerBruch
    return ergebnis

def schreibeKuerzen(bruch: Bruch) -> str:
    bruchGekuerzt = bruch.kuerze()
    textUngekuerzt = schreibeBruch(bruch)
    textGekuerzt = schreibeBruch(bruchGekuerzt)
    ergebnis = textUngekuerzt + "<mo>=</mo>" + textGekuerzt
    return ergebnis

def schreibeBruchZuDezimalzahl(bruch: Bruch) -> str:
    dezimalzahl = bruch.berechneDezimalzahl()
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    ergebnis = textBruch + "<mo>=</mo>" + textDezimalzahl
    return ergebnis

def vonDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> str:
    bruch = dezimalzahl.berechneBruch()
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    ergebnis = textDezimalzahl + "<mo>=</mo>" + textBruch
    return ergebnis