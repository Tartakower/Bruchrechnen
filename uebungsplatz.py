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

bruch = Bruch(6,8)
gekuerzter_bruch = mathehelfer.kuerzeBruch(bruch)
print("Kürzen: " + str(gekuerzter_bruch))

bruch = Bruch(2,3)
erweiterter_bruch = mathehelfer.erweitereBruch(bruch,3)
print("Erweitern: " + str(erweiterter_bruch))

erster_faktor = Bruch(3,4)
zweiter_faktor = Bruch(2,3)
produkt = mathehelfer.multipliziereBrueche(erster_faktor, zweiter_faktor)
print("Produkt: " + str(produkt))

bruch = Bruch(2,3)
formel = mathehelfer.schreibeErweitern(bruch, 3)
print(formel)

bruch = Bruch(6,8)
formel = mathehelfer.schreibeKuerzen(bruch)
print(formel)