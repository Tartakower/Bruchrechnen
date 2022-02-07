"""  """
from Berechnung import Berechnung
from UnaererAusdruck import Bruch, DezimalZahl, GemischteZahl


def test_berechneBruch() -> None:

    bruch: Bruch = Bruch(1,2)
    berechnung: Berechnung = Berechnung(bruch)
    assert "(1,2) = 0.5" == berechnung.schreibeBerechnung()

    bruch = Bruch(3,2)
    berechnung = Berechnung(bruch)
    assert "(3,2) = 1 (1,2) = 1.5" == berechnung.schreibeBerechnung()

    bruch = Bruch(10,4)
    berechnung = Berechnung(bruch)
    assert "(10,4) = (5,2) = 2 (1,2) = 2.5" == berechnung.schreibeBerechnung()

def test_berechneGemischteZahl() -> None:

    gemischteZahl: GemischteZahl = GemischteZahl(2, Bruch(12,8))
    assert "2 (12,8) = 3 (4,8) = 3 (1,2) = (7,2) = 3.5" == Berechnung(gemischteZahl).schreibeBerechnung()

def test_berechneDezimalZahl():
    dezimalZahl: DezimalZahl = DezimalZahl(1.25)
    assert "1.25 = (125,100) = (5 * 25,4 * 25) = (5,4) = 1 (1,4)" == Berechnung(dezimalZahl).schreibeBerechnung()