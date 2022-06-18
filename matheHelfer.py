from __future__ import annotations

from datenstrukturen import Bruch, Dezimalzahl
from mathefunktionen import berechne_ggT, berechne_ZehnerPotenz

def berechneBruchWert(bruch: Bruch) -> float:
    ergebnis = bruch.zaehler / bruch.nenner
    return ergebnis

def erweitereBruch(bruch: Bruch, faktor: int) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    neuerZaehler = alterZaehler * faktor
    neuerNenner = alterNenner * faktor
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

def kuerzeBruch(bruch: Bruch) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    kuerzungsFaktor = berechne_ggT(alterZaehler, alterNenner)
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
    neuerNenner = berechne_ZehnerPotenz(dezimalwert)
    neuerZaehler = int(dezimalwert * neuerNenner)
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

# Funktionen für MathML

def schreibeBruch(bruch: Bruch) -> str:
    zaehlerAlsString = str(bruch.zaehler)
    nennerAlsString = str(bruch.nenner)
    ergebnis = "<mfrac>"
    ergebnis = ergebnis + "<mi>" + zaehlerAlsString + "</mi>"
    ergebnis = ergebnis + "<mi>" + nennerAlsString + "</mi>"
    ergebnis = ergebnis + "</mfrac>"
    return ergebnis

def schreibeDezimalzahl(dezimalzahl: Dezimalzahl) -> str:
    dezimalwert = dezimalzahl.kommazahl
    zahlAlsString = str(dezimalwert)
    return "<mn>" + zahlAlsString + "</mn>"

def schreibeErweitern(bruch: Bruch, faktor: int) -> str:
    bruchErweitert = erweitereBruch(bruch, faktor)
    textAlterBruch = schreibeBruch(bruch)
    textNeuerBruch = schreibeBruch(bruchErweitert)
    return textAlterBruch + "<mo>=</mo>" + textNeuerBruch

def schreibeKuerzen(bruch: Bruch) -> str:
    bruchGekuerzt = kuerzeBruch(bruch)
    textUngekuerzt = schreibeBruch(bruch)
    textGekuerzt = schreibeBruch(bruchGekuerzt)
    return textUngekuerzt + "<mo>=</mo>" + textGekuerzt

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
    inhalt = "<p><math><mi>2</mi><mo>+</mo><mi>3</mi><mo>=</mo><mi>5</mi></math></p>"
    bruch = Bruch(3,4)
    inhalt += "\n\t\t<p><math>"
    inhalt += schreibeBruch(bruch)
    inhalt += "</math></p>"
    inhalt += "\n\t\t<p><math>"
    inhalt += schreibeErweitern(bruch, 3)
    inhalt += "</math></p>"

    bruchUngekuerzt: Bruch = Bruch(6,8)
    inhalt += "\n\t\t<p><math>"
    inhalt += schreibeKuerzen(bruchUngekuerzt)
    inhalt += "</math></p>"
    inhalt += "\n\t\t<p>"
    inhalt += vonBruchZuDezimalzahl(bruch)
    inhalt += "</p>\n\t\t<p>"
    inhalt += vonDezimalzahlZuBruch(Dezimalzahl(0.25))
    inhalt += "</p>"
    return inhalt