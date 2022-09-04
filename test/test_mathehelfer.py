from datenstrukturen import Bruch
import mathefunktionen
import mathehelferLoesung

def test_berechne_ggT() -> None:
    assert 252 == mathefunktionen.berechne_ggT(3528,3780)

def test_Bruch() -> None:
    assert Bruch(2,3) == Bruch(2,3)
    assert "Bruch(zaehler=2, nenner=3)" == str(Bruch(2,3))

def test_kuerzeBruch() -> None:
    assert Bruch(2,3) == mathehelferLoesung.kuerzeBruch(Bruch(6,9))
    
def test_erweitereBruch() -> None:
    assert Bruch(6,15) == mathehelferLoesung.erweitereBruch(Bruch(2,5), 3)

def test_schreibeBruch() -> None:
    assert "<mfrac><mn>3</mn><mn>4</mn></mfrac>" == mathehelferLoesung.schreibeBruch(Bruch(3,4))

def test_schreibeErweitern() -> None:
    assert "<mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>15</mn></mfrac>" == mathehelferLoesung.schreibeErweitern(Bruch(2,5), 3)

def test_schreibeKuerzen() -> None:
    assert "<mfrac><mn>6</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac>" == mathehelferLoesung.schreibeKuerzen(Bruch(6,8))