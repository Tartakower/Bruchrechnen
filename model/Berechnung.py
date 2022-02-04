"""  """

from abc import abstractmethod
from Ausdruck import Ausdruck
from typing import List


class Berechnung(object):

    def __init__(self, ausdruck: Ausdruck) -> None:
        self.__start = ausdruck
        self.__berechnung: List[Ausdruck] = []

    @property
    def berechnung(self) -> List[Ausdruck]:
        return self.__berechnung

    def __str__(self) -> str:
        if not self.istBerechnungErfolgt():
            self.berechne()

        length = len(self.__berechnung)
        result = str(self.__berechnung[0])
        for index in range(1, length):
            result += " = " + str(self.__berechnung[index])
        return result

    def getStart(self) -> Ausdruck:
        return self.__start

    def append(self, ausdruck: Ausdruck) -> None:
        self.__berechnung.append(ausdruck)

    def istBerechnungErfolgt(self) -> bool:
        return self.__berechnung

    @abstractmethod
    def berechne(self) -> None:
        pass

    def mathML(self) -> str:
        return ""