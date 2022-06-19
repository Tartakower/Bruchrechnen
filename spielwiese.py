from datenstrukturen import Bruch
from matheHelfer import berechneKehrwert, erweitereBruch


bruch_1 = Bruch(2,3)
bruch_2 = erweitereBruch(bruch_1,3)
print(bruch_2)

bruch_1 = Bruch(2,5)
kehrwert = berechneKehrwert(bruch_1)
print(kehrwert)