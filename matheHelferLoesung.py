from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Bruch():

    zaehler: int
    nenner: int

    def __str__(self: Bruch) -> str:
        return "Zähler: " + str(self.zaehler) + ", Nenner: " + str(self.nenner)

@dataclass(frozen=True)
class Dezimalzahl():

    kommazahl: float

    def __str__(self: Dezimalzahl) -> str:
        return "Kommazahl: " + str(self.kommazahl)

# Ende der Klassendefinitionen

# Beginn der mathematischen Hilfsfunktionen
def ggT(a: int, b: int) -> int:
    while b != 0:
        h = a % b
        a = b
        b = h
    return a

def berechneZehnerPotenz(zahl: float) -> int:
    zahlAlsString = str(zahl)
    nachkommastellen: str = zahlAlsString.partition(".")[2]
    anzahlNachkommastellen = len(nachkommastellen)
    ergebnis = pow(10,anzahlNachkommastellen)
    return ergebnis

# Ende der mathematischen Hilffunktionen

def berechneBruchWert(bruch: Bruch) -> float:
    ergebnis = bruch.zaehler / bruch.nenner
    return ergebnis

def kuerzeBruch(bruch: Bruch) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    kuerzungsFaktor = ggT(alterZaehler, alterNenner)
    neuerZaehler = alterZaehler // kuerzungsFaktor
    neuerNenner = alterNenner // kuerzungsFaktor
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

def wandleBruchZuDezimalzahl(bruch: Bruch) -> Dezimalzahl:
    wert = berechneBruchWert(bruch)
    return Dezimalzahl(wert)

def berecheDezimalzahlWert(dezimalzahl: Dezimalzahl) -> float:
    ergebnis = dezimalzahl.kommazahl
    return ergebnis

def wandleDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> Bruch:
    dezimalwert = dezimalzahl.kommazahl
    neuerNenner = berechneZehnerPotenz(dezimalwert)
    neuerZaehler = int(dezimalwert * neuerNenner)
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

# Funktionen für MathML

def schreibeBruch(bruch: Bruch) -> str:
    zaehlerAlsString = str(bruch.zaehler)
    nennerAlsString = str(bruch.nenner)
    ergebnis = "<mfrac><mi>" + zaehlerAlsString + "</mi><mi>" + nennerAlsString + "</mi></mfrac>"
    return ergebnis

def schreibeDezimalzahl(dezimalzahl: Dezimalzahl) -> str:
    dezimalwert = dezimalzahl.kommazahl
    zahlAlsString = str(dezimalwert)
    return "<mn>" + zahlAlsString + "</mn>"

def schreibeKuerzen(bruch: Bruch) -> str:
    bruchGekuerzt = kuerzeBruch(bruch)
    textUngekuerzt = schreibeBruch(bruch)
    textGekuerzt = schreibeBruch(bruchGekuerzt)
    return "<math>" + textUngekuerzt + "<mo>=</mo>" + textGekuerzt + "</math>"

def vonBruchZuDezimalzahl(bruch: Bruch) -> str:
    dezimalzahl = wandleBruchZuDezimalzahl(bruch)
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    return "<math>" + textBruch + "<mo>=</mo>" + textDezimalzahl + "</math>"

def vonDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> str:
    bruch = wandleDezimalzahlZuBruch(dezimalzahl)
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    return "<math>" + textDezimalzahl + "<mo>=</mo>" + textBruch + "</math>"

# In dieser Funktion darf ausprobiert werden.

def schreibeMathML() -> str:
    bruchUngekuerzt: Bruch = Bruch(6,8)
    bruch: Bruch = Bruch(3,4)
    inhalt = "<p>" 
    inhalt += schreibeKuerzen(bruchUngekuerzt)
    inhalt += "</p>\n\t\t<p>"
    inhalt += vonBruchZuDezimalzahl(bruch)
    inhalt += "</p>\n\t\t<p>"
    inhalt += vonDezimalzahlZuBruch(Dezimalzahl(0.25))
    inhalt += "</p>"
    return inhalt