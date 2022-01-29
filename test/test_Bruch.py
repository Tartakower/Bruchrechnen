import pytest
from Bruch import Bruch

def test_constructor() -> None:
    
    with pytest.raises(ZeroDivisionError):
        Bruch(1,0)
        
    bruch = Bruch(3,4)
    assert 3 == bruch.zaehler
    assert 4 == bruch.nenner
    
    bruch = Bruch(3,-4) 
    assert -3 == bruch.zaehler
    assert 4 == bruch.nenner   
        

def test_berechne() -> None:
    bruch = Bruch(3,4)
    assert bruch.berechneDezimalzahl() == 0.75
