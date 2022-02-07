"""  """

from abc import abstractmethod
from typing import cast, List
from Ausdruck import Ausdruck
from TemporaererAusdruck import MultBruch
from UnaererAusdruck import Bruch,  GemischteZahl, DezimalZahl


class BerechnungAusdruck(object):

    def __init__(self, ausdruck: Ausdruck) -> None:
        self.__ausdruck = ausdruck

    def getAusdruck(self) -> Ausdruck:
        return self.__ausdruck

    @abstractmethod  
    def berechne(self) -> List[Ausdruck]:
        pass

class BerechnungBruch(BerechnungAusdruck):

    def __init__(self, ausdruck: Bruch) -> None:
        super().__init__(ausdruck)

    def getAusdruck(self) -> Bruch:
        return cast(Bruch, super().getAusdruck())

    def berechne(self) -> List[Ausdruck]:
        bruch: Bruch = self.getAusdruck()
        berechnung: List[Ausdruck] = [bruch]
        if not bruch.istGekuerzt():
            bruch = bruch.kuerze()
            berechnung.append(bruch)
        if not bruch.istEchterBruch():
            gemischteZahl: GemischteZahl = bruch.berechneGemischteZahl()
            berechnung.append(gemischteZahl)
        berechnung.append(bruch.berechneDezimalzahl())
        return berechnung

class BerechnungGemischteZahl(BerechnungAusdruck):

    def __init__(self, ausdruck: GemischteZahl) -> None:
        super().__init__(ausdruck)

    def getAusdruck(self) -> GemischteZahl:
        return cast(GemischteZahl, super().getAusdruck())

    def berechne(self) -> List[Ausdruck]:
        zahl: GemischteZahl = self.getAusdruck()
        berechnung: List[Ausdruck] = [zahl]
        if not zahl.istEcht():
            zahl = zahl.extrahiereGanzzahl()
            berechnung.append(zahl)
        if not zahl.istGekuerzt():
            zahl = zahl.kuerze()
            berechnung.append(zahl)
        bruch: Bruch = zahl.berechneBruch()
        berechnung.append(bruch)
        berechnung.append(bruch.berechneDezimalzahl())
        return berechnung

class BerechnungDezimalZahl(BerechnungAusdruck):

    def __init__(self, ausdruck: DezimalZahl) -> None:
        super().__init__(ausdruck)

    def getAusdruck(self) -> DezimalZahl:
        return cast(DezimalZahl, super().getAusdruck())

    def berechne(self) -> List[Ausdruck]:
        zahl: DezimalZahl = self.getAusdruck()
        berechnung: List[Ausdruck] = [zahl]
        bruch: Bruch = zahl.berechneBruch(False)
        berechnung.append(bruch)
        multBruch: MultBruch = MultBruch.erzeugeErweiterung(bruch)
        berechnung.append(multBruch)
        bruch = bruch.kuerze()
        berechnung.append(bruch)
        if not bruch.istEchterBruch():
            berechnung.append(bruch.berechneGemischteZahl())
        return berechnung