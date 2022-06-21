# Ab hier bitte nichts ändern!
from __future__ import annotations

from datenstrukturen import Bruch
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
    ggT = mathefunktionen.berechne_ggT(alterZaehler, alterNenner)
    neuerZaehler = alterZaehler // ggT
    neuerNenner = alterNenner // ggT
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
    bruch = Bruch(6,8)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeKuerzen(bruch)
    inhalt = inhalt + "</math></p>"
    return inhalt