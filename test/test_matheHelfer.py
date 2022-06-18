from matheHelfer import Bruch, berechne_ggT, erweitereBruch, schreibeBruch, schreibeErweitern, schreibeKuerzen

def test_berechne_ggT() -> None:
    assert 252 == berechne_ggT(3528,3780)

def test_Bruch() -> None:
    assert Bruch(2,3) == Bruch(2,3)
    assert "Bruch(zaehler=2, nenner=3)" == str(Bruch(2,3))

def test_erweitereBruch() -> None:
    assert Bruch(6,15) == erweitereBruch(Bruch(2,5), 3)

def test_schreibeBruch() -> None:
    assert "<mfrac><mi>3</mi><mi>4</mi></mfrac>" == schreibeBruch(Bruch(3,4))

def test_schreibeErweitern() -> None:
    assert "<mfrac><mi>2</mi><mi>5</mi></mfrac><mo>=</mo><mfrac><mi>6</mi><mi>15</mi></mfrac>" == schreibeErweitern(Bruch(2,5), 3)

def test_schreibeKuerzen() -> None:
    assert "<mfrac><mi>6</mi><mi>8</mi></mfrac><mo>=</mo><mfrac><mi>3</mi><mi>4</mi></mfrac>" == schreibeKuerzen(Bruch(6,8))