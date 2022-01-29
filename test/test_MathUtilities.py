'''
Created on 27.01.2022

@author: norbert
'''
from MathUtilities import ggT, kgV

def test_ggT() -> None:
    
    assert 1 == ggT(1,6)
    assert 1 == ggT(5,1)
    
    assert 1 == ggT(13,17)
    
    assert 4 == ggT(44,12)
    
def test_kgV() -> None:
    
    assert 20 == kgV(-4,5)
    assert 12 == kgV(4,6)