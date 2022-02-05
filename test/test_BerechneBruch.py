"""  """
from Berechnung import Berechnung
from UnaererAusdruck import Bruch


def test_toString() -> None:

    bruch: Bruch = Bruch(1,2)
    berechnung: Berechnung = Berechnung(bruch)
    assert "(1,2) = 0.5" == berechnung.schreibeBerechnung()

    bruch = Bruch(3,2)
    berechnung = Berechnung(bruch)
    assert "(3,2) = 1 (1,2) = 1.5" == berechnung.schreibeBerechnung()

    bruch = Bruch(10,4)
    berechnung = Berechnung(bruch)
    assert "(10,4) = (5,2) = 2 (1,2) = 2.5" == berechnung.schreibeBerechnung()