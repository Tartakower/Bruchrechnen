"""  """

from typing import cast
from Berechnung import Berechnung
from UnaererAusdruck import Bruch, GemischteZahl


class BerechnungBruch(Berechnung):

    def __init__(self, ausdruck: Bruch) -> None:
        super().__init__(ausdruck)

    def __str__(self) -> str:
        return super().__str__()

    def getStart(self) -> Bruch:
        return cast(Bruch, super().getStart())

    def berechne(self) -> None:
        ausdruck: Bruch = self.getStart()
        self.append(ausdruck)
        if not ausdruck.istGekuerzt():
            ausdruck = ausdruck.kuerze()
            self.append(ausdruck)
        if not ausdruck.istEchterBruch():
            gemischteZahl: GemischteZahl = ausdruck.berechneGemischteZahl()
            self.append(gemischteZahl)
        self.append(ausdruck.berechneDezimalzahl())