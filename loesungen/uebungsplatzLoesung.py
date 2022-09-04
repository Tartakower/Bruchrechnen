from datenstrukturen import Bruch
import mathehelferLoesung

formel = "<math>"
formel = formel + "<mn>2</mn>"
formel = formel + "<mo>+</mo>"
formel = formel + "<mn>3</mn>"
formel = formel + "<mo>=</mo>"
formel = formel + "<mn>5</mn>"
formel = formel + "</math>"
print(formel)

bruch = Bruch(6,8)
gekuerzter_bruch = mathehelferLoesung.kuerzeBruch(bruch)
print("Kürzen: " + str(gekuerzter_bruch))

bruch = Bruch(2,3)
erweiterter_bruch = mathehelferLoesung.erweitereBruch(bruch,3)
print("Erweitern: " + str(erweiterter_bruch))

erster_faktor = Bruch(3,4)
zweiter_faktor = Bruch(2,3)
produkt = mathehelferLoesung.multipliziereBrueche(erster_faktor, zweiter_faktor)
print("Produkt: " + str(produkt))

bruch = Bruch(2,3)
formel = mathehelferLoesung.schreibeErweitern(bruch, 3)
print(formel)

bruch = Bruch(6,8)
formel = mathehelferLoesung.schreibeKuerzen(bruch)
print(formel)