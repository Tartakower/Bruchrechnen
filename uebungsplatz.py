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

formel = mathehelfer.schreibeMathML()
print(formel)

bruch = Bruch(6,8)
print(bruch)
# gekuerzter_bruch = ...
# print("Kürzen: " + str(gekuerzter_bruch))