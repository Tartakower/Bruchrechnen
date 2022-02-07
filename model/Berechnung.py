"""  """

from Ausdruck import Ausdruck
from typing import List

from BerechnungAusdruck import BerechnungAusdruck


class Berechnung(object):

    def __init__(self, ausdruck: Ausdruck) -> None:
        self.__ausdruck = ausdruck
        self.__berechnung: List[Ausdruck] = []

    @property
    def ausdruck(self) -> Ausdruck:
        return self.__ausdruck

    @property
    def berechnung(self) -> List[Ausdruck]:
        return self.__berechnung

    def __str__(self) -> str:
        return str(self.__ausdruck)

    def schreibeBerechnung(self) -> str:
        if not self.istBerechnungErfolgt():
            self.__berechnung.extend(self.berechne())

        length = len(self.__berechnung)
        result = str(self.__berechnung[0])
        for index in range(1, length):
            result += " = " + str(self.__berechnung[index])
        return result

    def istBerechnungErfolgt(self) -> bool:
        return bool(self.__berechnung)

    def berechne(self) -> List[Ausdruck]:
        berechnung: BerechnungAusdruck = self.__ausdruck.erzeugeBerechnung()
        return berechnung.berechne()

    def mathML(self) -> str:
        return ""