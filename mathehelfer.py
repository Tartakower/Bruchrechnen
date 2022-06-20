# Ab hier bitte nichts ändern!
from __future__ import annotations

from datenstrukturen import Bruch, Dezimalzahl
import mathefunktionen

# Ab hier dürft ihr Änderungen vornehmen.

def erweitereBruch(bruch: Bruch, faktor: int) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    neuerZaehler = alterZaehler * faktor
    neuerNenner = alterNenner * faktor
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

def berechneKehrwert(bruch: Bruch) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    neuerZaehler = alterNenner
    neuerNenner = alterZaehler
    kehrwert = Bruch(neuerZaehler, neuerNenner)
    return kehrwert

def kuerzeBruch(bruch: Bruch) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    ggT = mathefunktionen.berechne_ggT(alterZaehler, alterNenner)
    neuerZaehler = alterZaehler // ggT
    neuerNenner = alterNenner // ggT
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

def wandleBruchZuDezimalzahl(bruch: Bruch) -> Dezimalzahl:
    wert = bruch.zaehler / bruch.nenner
    return Dezimalzahl(wert)

def wandleDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> Bruch:
    dezimalwert = dezimalzahl.kommazahl
    neuerNenner = mathefunktionen.berechne_ZehnerPotenz(dezimalwert)
    neuerZaehler = int(dezimalwert * neuerNenner)
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

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
    bruchErweitert = erweitereBruch(bruch, faktor)
    textAlterBruch = schreibeBruch(bruch)
    textNeuerBruch = schreibeBruch(bruchErweitert)
    ergebnis = textAlterBruch + "<mo>=</mo>" + textNeuerBruch
    return ergebnis

def schreibeKuerzen(bruch: Bruch) -> str:
    bruchGekuerzt = kuerzeBruch(bruch)
    textUngekuerzt = schreibeBruch(bruch)
    textGekuerzt = schreibeBruch(bruchGekuerzt)
    ergebnis = textUngekuerzt + "<mo>=</mo>" + textGekuerzt
    return ergebnis

def vonBruchZuDezimalzahl(bruch: Bruch) -> str:
    dezimalzahl = wandleBruchZuDezimalzahl(bruch)
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    ergebnis = textBruch + "<mo>=</mo>" + textDezimalzahl
    return ergebnis

def vonDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> str:
    bruch = wandleDezimalzahlZuBruch(dezimalzahl)
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    ergebnis = textDezimalzahl + "<mo>=</mo>" + textBruch
    return ergebnis

# In dieser Funktion darf ausprobiert werden.

def schreibeMathML() -> str:
    inhalt = "<p><math><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p>"
    bruch = Bruch(3,4)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeBruch(bruch)
    inhalt = inhalt + "</math></p>"
    bruch = Bruch(3,4)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeErweitern(bruch, 3)
    inhalt = inhalt + "</math></p>"
    bruchUngekuerzt = Bruch(6,8)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeKuerzen(bruchUngekuerzt)
    inhalt = inhalt + "</math></p>"
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + vonBruchZuDezimalzahl(bruch)
    inhalt = inhalt +  "</math></p>"
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + vonDezimalzahlZuBruch(Dezimalzahl(0.25))
    inhalt = inhalt + "</math></p>"
    return inhalt