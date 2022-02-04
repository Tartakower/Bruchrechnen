"""  """
from BerechnungBruch import BerechnungBruch
from UnaererAusdruck import Bruch


def test_toString() -> None:

    bruch: Bruch = Bruch(1,2)
    berechneBruch: BerechnungBruch = BerechnungBruch(bruch)
    assert "1 / 2 = 0.5" == str(berechneBruch)