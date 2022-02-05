"""  """

from Ausdruck import BinaererAusdruck
from Operator import Operator

from TemporaererAusdruck import MultBruch


def test_toString() -> None:

    bruch_1: MultBruch = MultBruch(1, 2, 3, 4)
    assert "(1 * 3,2 * 4)" == str(bruch_1)

    bruch_2: MultBruch = MultBruch(5, 6, 7, 8)
    assert "(5 * 7,6 * 8)" == str(bruch_2)

    binaerBruch: BinaererAusdruck = BinaererAusdruck(Operator.PLUS, bruch_1, bruch_2)
    assert "(1 * 3,2 * 4) + (5 * 7,6 * 8)" == str(binaerBruch)