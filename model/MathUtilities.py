'''
Created on 27.01.2022

@author: norbert
'''

def ggT(a: int, b: int) -> int:
    while b != 0:
        h = a % b
        a = b
        b = h
    return a

def kgV(a: int, b: int) -> int:
    return abs(a * b) // ggT(a, b)