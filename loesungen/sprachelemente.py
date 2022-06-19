from datenstrukturen import Bruch
from matheHelfer import erweitereBruch


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