from __future__ import annotations

class Bruch():

    def __init__(self, zaehler: int, nenner: int):
        self.zaehler = zaehler
        self.nenner = nenner

class Dezimalzahl():

    def __init__(self, zahl: float):
        self.zahl = zahl

# Ende der Klassendefinitionen

def ggT(a: int, b: int) -> int:
    while b != 0:
        h = a % b
        a = b
        b = h
    return a

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
    ergebnis = dezimalzahl.zahl
    return ergebnis

def wandleDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> Bruch:
    dezimalwert = dezimalzahl.zahl
    zahlAlsString = str(dezimalwert)
    nachkommastellen: str = zahlAlsString.partition(".")[2]
    anzahlNachkommastellen = len(nachkommastellen)
    neuerNenner = pow(10,anzahlNachkommastellen)
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
    dezimalwert = dezimalzahl.zahl
    zahlAlsString = str(dezimalwert)
    return "<mn>" + zahlAlsString + "</mn>"

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
    bruch: Bruch = Bruch(3,4)
    inhalt = "<p>" 
    inhalt += vonBruchZuDezimalzahl(bruch)
    inhalt += "</p>\n\t\t<p>"
    inhalt += vonDezimalzahlZuBruch(Dezimalzahl(0.25))
    inhalt += "</p>"
    return inhalt