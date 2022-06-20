
import mathehelfer

htmlTitel = "\n\t\t<title>Bruchrechnen</title>"
htmlHead = "\n\t<head>\n\t\t<meta charset=\"utf-8\">\n\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" + htmlTitel + "\n\t</head>"

def schreibeHTML() -> str:
    htmlString = "<!doctype html>\n<html lang=\"de\">" + htmlHead + "\n\t<body>"
    htmlString += "\n\t\t" + mathehelfer.schreibeMathML()
    htmlString += "\n\t</body>\n</html>"
    return htmlString

def schreibeDatei() -> None:
    try:
        datei = open("index.html", "wt")
        datei.write(schreibeHTML())
        datei.close()
    except BaseException as err:
        print("Fehler: ", err)

schreibeDatei()