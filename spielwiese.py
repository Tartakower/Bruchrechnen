from datenstrukturen import Bruch
from matheHelfer import berechneKehrwert, erweitereBruch, schreibeErweitern, schreibeKuerzen


bruch_1 = Bruch(2,3)
bruch_2 = erweitereBruch(bruch_1,3)
print(bruch_2)

bruch_1 = Bruch(2,5)
kehrwert = berechneKehrwert(bruch_1)
print(kehrwert)

bruch = Bruch(2,3)
formel = schreibeErweitern(bruch, 3)
print(formel)

bruch = Bruch(6,8)
formel = schreibeKuerzen(bruch)
print(formel)