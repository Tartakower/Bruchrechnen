"""  """

from Ausdruck import Ausdruck
from BinaererAusdruck import Division, Multiplikation, Summe
from UnaererAusdruck import Bruch, DezimalZahl, GemischteZahl
from BerechnungAusdruck import *


class BerechnungsFactory(object):

    @staticmethod
    def erzeugeBerechungAusdruck(ausdruck: Ausdruck) -> BerechnungAusdruck:
        if isinstance(ausdruck, Bruch):
            return BerechnungBruch(ausdruck)
        if isinstance(ausdruck, GemischteZahl):
            return BerechnungGemischteZahl(ausdruck)
        if isinstance(ausdruck, DezimalZahl):
            return BerechnungDezimalZahl(ausdruck)
        if isinstance(ausdruck, Summe):
            return BerechnungSumme(ausdruck)
        if isinstance(ausdruck, Multiplikation):
            return BerechnungMultiplikation(ausdruck)
        if isinstance(ausdruck, Division):
            return BerechnungDivision(ausdruck)
        raise TypeError