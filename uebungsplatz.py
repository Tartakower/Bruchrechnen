from datenstrukturen import Bruch
from mathehelfer import berechneKehrwert, erweitereBruch, schreibeErweitern, schreibeKuerzen


bruch_1 = Bruch(2,3)
bruch_2 = erweitereBruch(bruch_1,3)
print(bruch_2)

bruch = Bruch(2,5)
kehrwert = berechneKehrwert(bruch)
print(kehrwert)

bruch = Bruch(2,3)
formel = schreibeErweitern(bruch, 3)
print(formel)

bruch = Bruch(6,8)
formel = schreibeKuerzen(bruch)
print(formel)

formel = "<math>"
formel = formel + "<mn>2</mn>"
formel = formel + "<mo>+</mo>"
formel = formel + "<mn>3</mn>"
formel = formel + "<mo>=</mo>"
formel = formel + "<mn>5</mn>"
formel = formel + "</math>"
print(formel)