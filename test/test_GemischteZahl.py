
from UnaererAusdruck import Bruch, GemischteZahl

def test_berechneBruch() -> None:
    assert Bruch(35,6) == GemischteZahl(5, Bruch(5,6)).berechneBruch()

def test_normiere() -> None:
    gemischteZahl: GemischteZahl = GemischteZahl(2, Bruch(12,8))
    normierteZahl: GemischteZahl = gemischteZahl.normiere()
    assert 3 == normierteZahl.ganzzahl
    assert Bruch(1,2) == normierteZahl.bruch
    assert 2 == gemischteZahl.ganzzahl
    assert Bruch(12,8) == gemischteZahl.bruch
