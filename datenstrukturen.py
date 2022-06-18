from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Bruch():

    zaehler: int
    nenner: int

@dataclass(frozen=True)
class Dezimalzahl():

    kommazahl: float

@dataclass(frozen=True)
class GemischteZahl():

    ganzzahl: int
    bruch: Bruch