# Ab hier bitte nichts ändern!
from __future__ import annotations

from datenstrukturen import Bruch
import mathefunktionen

mathefunktionen.berechne_ggT(1, 1)

def kopiereBruch(bruch: Bruch) -> Bruch:
    return Bruch(bruch.zaehler, bruch.nenner)

# Ab hier dürft ihr Änderungen vornehmen.

# Hier sollen die Funktionen zum Kürzen, Erweitern und Multiplizieren von Brüchen stehen.



# Funktionen für MathML

def schreibeBruch(bruch: Bruch) -> str:
    zaehlerAlsString = str(bruch.zaehler)
    nennerAlsString = str(bruch.nenner)
    ergebnis = "<mfrac>"
    ergebnis = ergebnis + "<mn>" + zaehlerAlsString + "</mn>"
    ergebnis = ergebnis + "<mn>" + nennerAlsString + "</mn>"
    ergebnis = ergebnis + "</mfrac>"
    return ergebnis


# In dieser Funktion wird die Darstellung für den Browser zusammengestellt.

def schreibeMathML() -> str:
    inhalt = "<p><math><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>5</mn></math></p>"
    bruch = Bruch(3,4)
    inhalt = inhalt + "\n\t\t<p><math>"
    inhalt = inhalt + schreibeBruch(bruch)
    inhalt = inhalt + "</math></p>"
    
    return inhalt