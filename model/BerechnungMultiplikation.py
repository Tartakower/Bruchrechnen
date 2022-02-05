"""  """

from typing import List, cast
from Ausdruck import Ausdruck, BinaererAusdruck
from Berechnung import Berechnung
from BerechnungBruch import BerechnungBruch
from Operator import Operator
from TemporaererAusdruck import MultBruch
from UnaererAusdruck import Bruch


class BerechnungMultiplikation(Berechnung):
    
    def __init__(self, ausdruck: BinaererAusdruck) -> None:
        super().__init__(ausdruck)

    def getStart(self) -> BinaererAusdruck:
        return cast(BinaererAusdruck, super().getStart())

    def berechne(self) -> List[Ausdruck]:
        ausdruck: BinaererAusdruck = self.getStart()
        berechnung: List[Ausdruck] = []
        berechnung.append(ausdruck)
        berechnung.extend(self.berechneProdukt(ausdruck))
        return berechnung

    def berechneSumme(self, ausdruck: BinaererAusdruck) -> None:
        pass

    def berechneDifferenz(self, ausdruck: BinaererAusdruck) -> None:
        pass

    def berechneProdukt(self, ausdruck: BinaererAusdruck) -> List[Ausdruck]:
        berechnung: List[Ausdruck] = []
        bruch_1: Bruch = cast(Bruch, ausdruck.operand_1)
        bruch_2: Bruch = cast(Bruch, ausdruck.operand_2)
        if not(bruch_1.istGekuerzt() and bruch_2.istGekuerzt()):
            bruch_1 = bruch_1.kuerze()
            bruch_2 = bruch_2.kuerze()
            berechnung.append(BinaererAusdruck(Operator.MULT, bruch_1, bruch_2))
        tempBruch: MultBruch = MultBruch.erzeugeMultBruch(bruch_1, bruch_2)
        berechnung.append(tempBruch)
        if not tempBruch.ist_kreuz_gekuerzt():
            tempBruch = tempBruch.kreuz_kuerzen()
            berechnung.append(tempBruch)
        bruch: Bruch = tempBruch.berechneBruch()
        berechnungBruch: BerechnungBruch = BerechnungBruch(bruch)
        berechnung.extend(berechnungBruch.berechne())
        return berechnung

    def berechneQuotient(self, ausdruck: BinaererAusdruck) -> None:
        pass