"""  """

from Ausdruck import BinaererAusdruck
from BerechnungMultiplikation import BerechnungMultiplikation
from Operator import Operator
from UnaererAusdruck import Bruch


def test_toString() -> None:

    bruch_1: Bruch = Bruch(6,8)
    bruch_2: Bruch = Bruch(2,5)
    mult = BinaererAusdruck(Operator.MULT, bruch_1, bruch_2)
    berechnung = BerechnungMultiplikation(mult)
    assert "(6,8) * (2,5) = (3,4) * (2,5) = (3 * 2,4 * 5) = (3 * 1,2 * 5)" == berechnung.schreibeBerechnung()