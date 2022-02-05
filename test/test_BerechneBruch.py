"""  """
from BerechnungBruch import BerechnungBruch
from UnaererAusdruck import Bruch


def test_toString() -> None:

    bruch: Bruch = Bruch(1,2)
    berechneBruch: BerechnungBruch = BerechnungBruch(bruch)
    assert "(1,2) = 0.5" == berechneBruch.schreibeBerechnung()

    bruch = Bruch(3,2)
    berechneBruch = BerechnungBruch(bruch)
    assert "(3,2) = 1 (1,2) = 1.5" == berechneBruch.schreibeBerechnung()

    bruch = Bruch(10,4)
    berechneBruch = BerechnungBruch(bruch)
    assert "(10,4) = (5,2) = 2 (1,2) = 2.5" == berechneBruch.schreibeBerechnung()