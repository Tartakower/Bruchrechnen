"""  """

from UnaererAusdruck import DezimalZahl


def test_berechneBruch() -> None:
    dezimalZahl: DezimalZahl = DezimalZahl(0.25)
    assert "(25,100)" == str(dezimalZahl.berechneBruch(False))
    assert "(1,4)" == str(dezimalZahl.berechneBruch(True))
    