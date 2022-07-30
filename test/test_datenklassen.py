from loesungen.datenklassen import Bruch, Dezimalzahl, GemischteZahl


def test_berechneBruch() -> None:
    assert Bruch(2,3) == Bruch(2,3).berechneBruch()
    assert Bruch(3,4) == Dezimalzahl(0.75).berechneBruch()
    assert Bruch(67,12) == GemischteZahl(5, Bruch(7,12)).berechneBruch()
    assert Bruch(21,4) == GemischteZahl(5, Bruch(3,12)).berechneBruch()

def test_Bruch() -> None:
    assert Bruch(2,3) == Bruch(8,12).kuerze()
    assert Bruch(8,12) == Bruch(2,3).erweitere(4)