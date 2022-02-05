"""  """

from Ausdruck import Ausdruck
from typing import List


class Berechnung(object):

    def __init__(self, ausdruck: Ausdruck) -> None:
        self.__ausdruck = ausdruck
        self.__berechnung: List[Ausdruck] = []

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

    def getStart(self) -> Ausdruck:
        return self.__ausdruck

    def istBerechnungErfolgt(self) -> bool:
        return self.__berechnung is True

    def berechne(self) -> List[Ausdruck]:
        return self.__ausdruck.berechne()

    def mathML(self) -> str:
        return ""