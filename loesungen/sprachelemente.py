from datenstrukturen import Bruch
from mathehelfer import erweitereBruch


wichtige_zahl = 42
summe = 2 + 3
summe = summe + 6

bruch_1 = Bruch(3,4)
zaehler_1 = bruch_1.zaehler
nenner_1 = bruch_1.nenner

zaehler_2 = 7
nenner_2 = 8
bruch_2 = Bruch(zaehler_2, nenner_2)

bruch_2 = Bruch(1,2)
bruch_3 = erweitereBruch(bruch_2, 5)

eine_zeichenkette = "x2-d2"
berg = '8000er Gipfel'
ein_ganzer_satz = "Python ist toll!"

formel = "<math>"
formel = formel + "<mn>2</mn>"
formel = formel + "<mo>+</mo>"
formel = formel + "<mn>3</mn>"
formel = formel + "<mo>=</mo>"
formel = formel + "<mn>5</mn>"
formel = formel + "</math>"