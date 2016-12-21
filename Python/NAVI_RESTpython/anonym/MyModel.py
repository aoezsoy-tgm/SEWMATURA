import requests
from xml.etree import ElementTree

class MyModel():
    """
    Model

    Beinhaltet die Logik bzw. die vom Controller benoetigten Attribute.
    In dieser Klasse befindet sich die Abfrage auf die Google-API.

    __version__ = '1.0'

    __author__ = 'Anonym'

    """
    def __init__(self,url="http://maps.googleapis.com/maps/api/directions/xml"):
        """
        Konstruktor zum Initalisieren
        Da werden benötigte Variablen erzeugt um auch in der Controller Klasse darauf zugreifen zu koennen.
        Die URL wurde als 'optionaler Parameter' angegeben, um moeglichst flexibel bei der Aenderung der API zu sein.

        :param url: die URL zur API
        """
        self.language="de"
        self.url = url
        self.status_code = ""
        self.ausgabe = ""
        self.start = ""
        self.ziel = ""

    def getRequest(self,start,ziel):
        """
        Diese Funktion wird verwendet für die Abfrage zur Google API.
        Mithilfe der Python Library "xml.etree' bzw. mithilfe von ElemenTrree die vom Google-Server erhaltene
        response, welche im XML - Format ist, geparsed.
        Um zu wissen, welche Attribute prinzipiell in der XML - Response vorhanden sind, kann man eine einfache Abfrage
        im Browser machen und sich die Response anschauen - dadurch erhaelt man die Struktur von der XML - Response
        z.B. http://maps.googleapis.com/maps/api/directions/xml?origin=Wien,Handleskai&destination=Wien,Floridsdorf

        :param start: Startadresse
        :param ziel: Zieladresse
        :return: Text zur Ausgabe
        """
        params = {"origin":start, "destination":ziel, "language":self.language}
        xml = requests.get(self.url, params)
        tree = ElementTree.fromstring(xml.text)
        status_code = tree.find("status").text

        if status_code == "OK":
            self.status_code = "BERECHNUNG: " + status_code
            route = tree[1]
            steps = ""
            for step in route.iter('step'):
                steps += step.find("./html_instructions").text + \
                         ", ENTFERNUNG: " + step.find("./distance/text").text +\
                                     ", DAUER: " + step.find("./duration/text").text +  "<br>"

            dauer = route.find("./leg/duration/text").text
            distanz = route.find("./leg/distance/text").text
            self.text = "Die GESAMTDAUER beträgt <b>" + dauer + "</b>, die GESAMTENTFERNUNG: <b>" + distanz + \
                        "</b> <br><br>" + steps
            return self.text

        elif status_code == "NOT_FOUND" or status_code == "NONE" or "ZERO_RESULTS":
            self.status_code = "FAILED: " + status_code
            return "Adresse oder Ort nicht gefunden: Geben sie BITTE eine gültige bzw. existierende Adresse oder Ort ein!!"
