# Ab hier bitte nichts ändern!
from __future__ import annotations

from datenstrukturen import Bruch
import mathefunktionen

# Ab hier dürft ihr Änderungen vornehmen.

def kuerzeBruch(bruch: Bruch) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    ggT = mathefunktionen.berechne_ggT(alterZaehler, alterNenner)
    neuerZaehler = alterZaehler // ggT
    neuerNenner = alterNenner // ggT
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

def erweitereBruch(bruch: Bruch, faktor: int) -> Bruch:
    alterZaehler = bruch.zaehler
    alterNenner = bruch.nenner
    neuerZaehler = alterZaehler * faktor
    neuerNenner = alterNenner * faktor
    neuerBruch = Bruch(neuerZaehler, neuerNenner)
    return neuerBruch

def multipliziereBrueche(erster_faktor: Bruch, zweiter_faktor: Bruch) -> Bruch:
    erster_zaehler = erster_faktor.zaehler
    erster_nenner = erster_faktor.nenner
    zweiter_zaehler = zweiter_faktor.zaehler
    zweiter_nenner = zweiter_faktor.nenner
    produkt_zaehler = erster_zaehler * zweiter_zaehler
    produkt_nenner = erster_nenner * zweiter_nenner
    produkt = Bruch(produkt_zaehler, produkt_nenner)
    produkt = kuerzeBruch(produkt)
    return produkt

# Funktionen für MathML

def schreibeBruch(bruch: Bruch) -> str:
    zaehlerAlsString = str(bruch.zaehler)
    nennerAlsString = str(bruch.nenner)
    ergebnis = "<mfrac>"
    ergebnis = ergebnis + "<mn>" + zaehlerAlsString + "</mn>"
    ergebnis = ergebnis + "<mn>" + nennerAlsString + "</mn>"
    ergebnis = ergebnis + "</mfrac>"
    return ergebnis

def schreibeKuerzen(bruch: Bruch) -> str:
    bruchGekuerzt = kuerzeBruch(bruch)
    textUngekuerzt = schreibeBruch(bruch)
    textGekuerzt = schreibeBruch(bruchGekuerzt)
    ergebnis = textUngekuerzt + "<mo>=</mo>" + textGekuerzt
    return ergebnis

def schreibeErweitern(bruch: Bruch, faktor: int) -> str:
    bruchErweitert = erweitereBruch(bruch, faktor)
    textAlterBruch = schreibeBruch(bruch)
    textNeuerBruch = schreibeBruch(bruchErweitert)
    ergebnis = textAlterBruch + "<mo>=</mo>" + textNeuerBruch
    return ergebnis

def schreibeMultiplikation(erster_faktor: Bruch, zweiter_faktor: Bruch) -> str:
    text_erster_faktor = schreibeBruch(erster_faktor)
    text_zweiter_faktor = schreibeBruch(zweiter_faktor)
    produkt = multipliziereBrueche(erster_faktor, zweiter_faktor)
    text_produkt = schreibeBruch(produkt)
    ergebnis = text_erster_faktor + "<mo>&middot;</mo>" + text_zweiter_faktor + "<mo>=</mo>" + text_produkt
    return ergebnis

# In dieser Funktion darf ausprobiert werden.

def schreibeMathML() -> str:
    inhalt = "<p><math><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p>"
    bruch = Bruch(3,4)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeBruch(bruch)
    inhalt = inhalt + "</math></p>"
    bruch = Bruch(6,8)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeKuerzen(bruch)
    inhalt = inhalt + "</math></p>"
    bruch = Bruch(3,4)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeErweitern(bruch, 3)
    inhalt = inhalt + "</math></p>"
    erster_faktor = Bruch(3,4)
    zweiter_faktor = Bruch(2,3)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeMultiplikation(erster_faktor, zweiter_faktor)
    inhalt = inhalt + "</math></p>"
    return inhalt