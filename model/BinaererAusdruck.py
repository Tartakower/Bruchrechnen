"""  """

from typing import List, cast
from Ausdruck import Ausdruck, BinaererAusdruck
from Berechnung import Berechnung
from MathUtilities import kgV
from Operator import Operator
from TemporaererAusdruck import MultBruch, SummenBruch
from UnaererAusdruck import Bruch

class BinaererBruchAusdruck(BinaererAusdruck):

    def __init__(self, operator: Operator, operand_1: Bruch, operand_2: Bruch) -> None:
        super().__init__(operator, operand_1, operand_2)

    def getOperand_1(self) -> Bruch:
        return cast(Bruch, self.operand_1)

    def getOperand_2(self) -> Bruch:
        return cast(Bruch, self.operand_2)

class Summe(BinaererBruchAusdruck):

    def __init__(self, operator: Operator, summand_1: Bruch, summand_2: Bruch) -> None:
        super().__init__(operator, summand_1, summand_2)

    def berechne(self) -> List[Ausdruck]:
        berechnung: List[Ausdruck] = [self]
        bruch_1: Bruch = self.getOperand_1()
        bruch_2: Bruch = self.getOperand_2()
        hauptnenner: int = kgV(bruch_1.nenner, bruch_2.nenner)
        faktor_1 = hauptnenner // bruch_1.nenner
        faktor_2 = hauptnenner // bruch_2.nenner
        summand_1: MultBruch = MultBruch(bruch_1.zaehler, bruch_1.nenner, faktor_1, faktor_1)
        summand_2: MultBruch = MultBruch(bruch_2.zaehler, bruch_2.nenner, faktor_2, faktor_2)
        ausdruck = BinaererAusdruck(self.operator, summand_1, summand_2)
        berechnung.append(ausdruck)
        sumBruch: SummenBruch = SummenBruch(self.operator, bruch_1.zaehler * faktor_1, bruch_2.zaehler * faktor_2, hauptnenner)
        berechnung.append(sumBruch)
        berechnung.extend(Berechnung(sumBruch.berechneBruch()).berechne())
        return berechnung

class Addition(Summe):

    def __init__(self, summand_1: Bruch, summand_2: Bruch) -> None:
        super().__init__(Operator.PLUS, summand_1, summand_2)
   
class Subtraktion(Summe):

    def __init__(self, summand_1: Bruch, summand_2: Bruch) -> None:
        super().__init__(Operator.MINUS, summand_1, summand_2)

class Multiplikation(BinaererBruchAusdruck):

    def __init__(self, faktor_1: Bruch, faktor_2: Bruch) -> None:
        super().__init__(Operator.MULT, faktor_1, faktor_2)
    
    def berechne(self) -> List[Ausdruck]:
        berechnung: List[Ausdruck] = [self]
        bruch_1: Bruch = self.getOperand_1()
        bruch_2: Bruch = self.getOperand_2()
        if not(bruch_1.istGekuerzt() and bruch_2.istGekuerzt()):
            bruch_1 = bruch_1.kuerze()
            bruch_2 = bruch_2.kuerze()
            berechnung.append(BinaererAusdruck(Operator.MULT, bruch_1, bruch_2))
        tempBruch: MultBruch = MultBruch.erzeugeMultBruch(bruch_1, bruch_2)
        berechnung.append(tempBruch)
        if not tempBruch.ist_kreuz_gekuerzt():
            tempBruch = tempBruch.kreuz_kuerzen()
            berechnung.append(tempBruch)
        berechnung.extend(Berechnung(tempBruch.berechneBruch()).berechne())
        return berechnung

class Division(BinaererBruchAusdruck):

    def __init__(self, faktor_1: Bruch, faktor_2: Bruch) -> None:
        super().__init__(Operator.DIV, faktor_1, faktor_2)

    def berechne(self) -> List[Ausdruck]:
        berechnung: List[Ausdruck] = [self]
        mult: Multiplikation = Multiplikation(self.getOperand_1(), self.getOperand_2().kehrwert())
        berechnung.extend(mult.berechne())
        return berechnung