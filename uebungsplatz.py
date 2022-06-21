from datenstrukturen import Bruch
import mathehelfer

formel = "<math>"
formel = formel + "<mn>2</mn>"
formel = formel + "<mo>+</mo>"
formel = formel + "<mn>3</mn>"
formel = formel + "<mo>=</mo>"
formel = formel + "<mn>5</mn>"
formel = formel + "</math>"
print(formel)

bruch_1 = Bruch(2,3)
bruch_2 = mathehelfer.erweitereBruch(bruch_1,3)
print(bruch_2)

bruch = Bruch(2,3)
formel = mathehelfer.schreibeErweitern(bruch, 3)
print(formel)

bruch = Bruch(6,8)
formel = mathehelfer.schreibeKuerzen(bruch)
print(formel)