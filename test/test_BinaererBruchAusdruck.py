"""  """

from Berechnung import Berechnung
from BinaererAusdruck import Addition, Division, Multiplikation, Subtraktion
from UnaererAusdruck import Bruch


def test_multiplikation() -> None:

    bruch_1: Bruch = Bruch(6,8)
    bruch_2: Bruch = Bruch(2,5)
    mult: Multiplikation = Multiplikation(bruch_1, bruch_2)
    berechnung = Berechnung(mult)
    assert "(6,8) * (2,5) = (3,4) * (2,5) = (3 * 2,4 * 5) = (3 * 1,2 * 5) = (3,10) = 0.3" == berechnung.schreibeBerechnung()

def test_division() -> None:

    bruch_1: Bruch = Bruch(6,8)
    bruch_2: Bruch = Bruch(5,2)
    div: Division = Division(bruch_1, bruch_2)
    berechnung = Berechnung(div)
    assert "(6,8) : (5,2) = (6,8) * (2,5) = (3,4) * (2,5) = (3 * 2,4 * 5) = (3 * 1,2 * 5) = (3,10) = 0.3" == berechnung.schreibeBerechnung()

def test_addition() -> None:

    bruch_1: Bruch = Bruch(1,2)
    bruch_2: Bruch = Bruch(2,5)
    summe: Addition = Addition(bruch_1, bruch_2)
    berechnung = Berechnung(summe)
    assert "(1,2) + (2,5) = (1 * 5,2 * 5) + (2 * 2,5 * 2) = (5 + 4,10) = (9,10) = 0.9" == berechnung.schreibeBerechnung()

def test_subtraktion() -> None:
    bruch_1: Bruch = Bruch(1,2)
    bruch_2: Bruch = Bruch(2,5)
    summe: Subtraktion = Subtraktion(bruch_1, bruch_2)
    berechnung = Berechnung(summe)
    assert "(1,2) - (2,5) = (1 * 5,2 * 5) - (2 * 2,5 * 2) = (5 - 4,10) = (1,10) = 0.1" == berechnung.schreibeBerechnung()