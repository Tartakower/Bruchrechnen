
# from TemporaererAusdruck import MultBruch
from UnaererAusdruck import Bruch, GemischteZahl

import pytest

def test_constructor() -> None:
    
    with pytest.raises(ZeroDivisionError):
        Bruch(1,0)
        
    bruch = Bruch(3,4)
    assert 3 == bruch.zaehler
    assert 4 == bruch.nenner
    
    bruch = Bruch(3,-4) 
    assert -3 == bruch.zaehler
    assert 4 == bruch.nenner   
        
def test_berechneWert() -> None:
    bruch = Bruch(3,4)
    assert bruch.berechneWert() == 0.75
    
def test_istEchterBruch() -> None:
    assert Bruch(5,6).istEchterBruch()
    assert not Bruch(7,7).istEchterBruch()
    assert not Bruch(9,8).istEchterBruch()

def test_istGekuerzt() -> None:
    assert Bruch(7, 22).istGekuerzt()
    assert not Bruch(17, 51).istGekuerzt()
    
def test_kuerze() -> None:
    assert Bruch(1,3) == Bruch(17, 51).kuerze()
    
def test_berechneGemischteZahl() -> None:
    assert GemischteZahl(5, Bruch(5,6)) == Bruch(70,12).berechneGemischteZahl()