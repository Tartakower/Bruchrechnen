'''
Created on 29.01.2022

@author: norbert
'''
from Grundrechnen import *

def test_berechne() -> None:
    assert 7 == Grundrechnen(Operator.PLUS, 3, 4).berechne()

def test_toString() -> None:
    assert "3 * 4" == str(Grundrechnen(Operator.MULT, 3, 4))

def test_mathML() -> None:
    assert "<mn>3</mn><mo>-</mo><mn>4</mn>" == Grundrechnen(Operator.MINUS, 3, 4).mathML()