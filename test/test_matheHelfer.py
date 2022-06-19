from datenstrukturen import Bruch, Dezimalzahl
import matheHelfer
import mathefunktionen

def test_berechne_ggT() -> None:
    assert 252 == mathefunktionen.berechne_ggT(3528,3780)

def test_Bruch() -> None:
    assert Bruch(2,3) == Bruch(2,3)
    assert "Bruch(zaehler=2, nenner=3)" == str(Bruch(2,3))

def test_wandleBruchZuDezimalzahl() -> None:
    assert Dezimalzahl(0.75) == matheHelfer.wandleBruchZuDezimalzahl(Bruch(3,4))

def test_erweitereBruch() -> None:
    assert Bruch(6,15) == matheHelfer.erweitereBruch(Bruch(2,5), 3)

def test_schreibeBruch() -> None:
    assert "<mfrac><mn>3</mn><mn>4</mn></mfrac>" == matheHelfer.schreibeBruch(Bruch(3,4))

def test_schreibeErweitern() -> None:
    assert "<mfrac><mn>2</mn><mn>5</mn></mfrac><mo>=</mo><mfrac><mn>6</mn><mn>15</mn></mfrac>" == matheHelfer.schreibeErweitern(Bruch(2,5), 3)

def test_schreibeKuerzen() -> None:
    assert "<mfrac><mn>6</mn><mn>8</mn></mfrac><mo>=</mo><mfrac><mn>3</mn><mn>4</mn></mfrac>" == matheHelfer.schreibeKuerzen(Bruch(6,8))

def test_vonBruchZuDezimalzahl() -> None:
    assert "<mfrac><mn>3</mn><mn>4</mn></mfrac><mo>=</mo><mn>0.75</mn>" == matheHelfer.vonBruchZuDezimalzahl(Bruch(3,4))

def test_vonDezimalzahlZuBruch() -> None:
    assert "<mn>0.25</mn><mo>=</mo><mfrac><mn>25</mn><mn>100</mn></mfrac>" == matheHelfer.vonDezimalzahlZuBruch(Dezimalzahl(0.25))