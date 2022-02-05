"""  """

from typing import List, cast
from Ausdruck import Ausdruck
from Berechnung import Berechnung
from UnaererAusdruck import Bruch, GemischteZahl


class BerechnungBruch(Berechnung):

    def __init__(self, ausdruck: Bruch) -> None:
        super().__init__(ausdruck)

    def getStart(self) -> Bruch:
        return cast(Bruch, super().getStart())

    def berechne(self) -> List[Ausdruck]:
        berechnung: List[Ausdruck] = []
        ausdruck: Bruch = self.getStart()
        berechnung.append(ausdruck)
        if not ausdruck.istGekuerzt():
            ausdruck = ausdruck.kuerze()
            berechnung.append(ausdruck)
        if not ausdruck.istEchterBruch():
            gemischteZahl: GemischteZahl = ausdruck.berechneGemischteZahl()
            berechnung.append(gemischteZahl)
        berechnung.append(ausdruck.berechneDezimalzahl())
        return berechnung