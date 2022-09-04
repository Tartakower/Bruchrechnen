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

def kuerzeBruch(bruch: Bruch) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    kuerzungsFaktor = mathefunktionen.berechne_ggT(alterZaehler, alterNenner)
    neuerZaehler = alterZaehler // kuerzungsFaktor
    neuerNenner = alterNenner // kuerzungsFaktor
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
    return textBruch + "<mo>=</mo>" + textDezimalzahl

def vonDezimalzahlZuBruch(dezimalzahl: Dezimalzahl) -> str:
    bruch = wandleDezimalzahlZuBruch(dezimalzahl)
    textBruch = schreibeBruch(bruch)
    textDezimalzahl = schreibeDezimalzahl(dezimalzahl)
    return textDezimalzahl + "<mo>=</mo>" + textBruch

# In dieser Funktion darf ausprobiert werden.

def schreibeMathML() -> str:
    inhalt = "<p><math><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p>"
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
    inhalt += "\n\t\t<p><math>"
    inhalt += vonBruchZuDezimalzahl(bruch)
    inhalt += "</math></p>"
    inhalt += "\n\t\t<p><math>"
    inhalt += vonDezimalzahlZuBruch(Dezimalzahl(0.25))
    inhalt += "</math></p>"
    return inhalt