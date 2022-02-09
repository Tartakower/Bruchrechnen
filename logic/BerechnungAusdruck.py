"""  """

from __future__ import division
from abc import abstractmethod
from typing import cast, List
from Ausdruck import Ausdruck, BinaererAusdruck
from MathUtilities import kgV
from Operator import Operator
from TemporaererAusdruck import MultBruch, SummenBruch
from UnaererAusdruck import Bruch,  GemischteZahl, DezimalZahl
from BinaererAusdruck import Division, Multiplikation, Summe


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

class BerechnungSumme(BerechnungAusdruck):

    def __init__(self, ausdruck: Summe) -> None:  
        super().__init__(ausdruck)

    def getAusdruck(self) -> Summe:   
        return cast(Summe, super().getAusdruck())

    def berechne(self) -> List[Ausdruck]:
        summe: Summe = self.getAusdruck()
        berechnung: List[Ausdruck] = [summe]
        bruch_1: Bruch = summe.getOperand_1()
        bruch_2: Bruch = summe.getOperand_2()
        hauptnenner: int = kgV(bruch_1.nenner, bruch_2.nenner)
        faktor_1 = hauptnenner // bruch_1.nenner
        faktor_2 = hauptnenner // bruch_2.nenner
        summand_1: MultBruch = MultBruch(bruch_1.zaehler, bruch_1.nenner, faktor_1, faktor_1)
        summand_2: MultBruch = MultBruch(bruch_2.zaehler, bruch_2.nenner, faktor_2, faktor_2)
        ausdruck = BinaererAusdruck(summe.operator, summand_1, summand_2)
        berechnung.append(ausdruck)
        sumBruch: SummenBruch = SummenBruch(summe.operator, bruch_1.zaehler * faktor_1, bruch_2.zaehler * faktor_2, hauptnenner)
        berechnung.append(sumBruch)
        berechnung.extend(BerechnungBruch(sumBruch.berechneBruch()).berechne())
        return berechnung

class BerechnungMultiplikation(BerechnungAusdruck):

    def __init__(self, ausdruck: Multiplikation) -> None:  
        super().__init__(ausdruck)

    def getAusdruck(self) -> Multiplikation:   
        return cast(Multiplikation, super().getAusdruck())

    def berechne(self) -> List[Ausdruck]:
        mult: Multiplikation = self.getAusdruck()
        berechnung: List[Ausdruck] = [mult]
        bruch_1: Bruch = mult.getOperand_1()
        bruch_2: Bruch = mult.getOperand_2()
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
        berechnung.extend(BerechnungBruch(bruch).berechne())
        return berechnung

class BerechnungDivision(BerechnungAusdruck):

    def __init__(self, ausdruck: Division) -> None:  
        super().__init__(ausdruck)

    def getAusdruck(self) -> Division:   
        return cast(Division, super().getAusdruck())

    def berechne(self) -> List[Ausdruck]:
        division: Division = self.getAusdruck()
        berechnung: List[Ausdruck] = [division]
        bruch_1: Bruch = division.getOperand_1()
        bruch_2: Bruch = division.getOperand_2().kehrwert()
        mult: Multiplikation = Multiplikation(bruch_1, bruch_2)
        berechnung.extend(BerechnungMultiplikation(mult).berechne())
        return berechnung