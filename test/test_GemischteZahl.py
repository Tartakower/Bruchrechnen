
from Bruch import Bruch
from GemischteZahl import GemischteZahl

def test_berechneBruch() -> None:
    assert Bruch(35,6) == GemischteZahl(5, Bruch(5,6)).berechneBruch()
