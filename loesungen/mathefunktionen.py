from __future__ import annotations

def berechne_ggT(a: int, b: int) -> int:
    while b != 0:
        (a,b) = (b, a % b)
    return a

def berechne_ZehnerPotenz(zahl: float) -> int:
    zahlAlsString = str(zahl)
    nachkommastellen: str = zahlAlsString.partition(".")[2]
    anzahlNachkommastellen = len(nachkommastellen)
    ergebnis = pow(10,anzahlNachkommastellen)
    return ergebnis