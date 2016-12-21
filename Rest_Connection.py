import requests
import sys
from PySide.QtGui import *
from PySide.QtCore import *
import gui as gui

class Verbindung(QWidget):
    """
    REST Google API
    """

    def __init__(self, parent=None):
        """
        init

        :param parent:
        """
        super().__init__(parent)
        self.myForm = gui.Ui_Navigation()
        self.myForm.setupUi(self)

    def get_google_driving_api(self, text, html=True):
        """
        get api

        :param text:
        :param html:
        :return:
        """
        resp = requests.get(
            "http://maps.googleapis.com/maps/api/directions/json?" + text).json()
        print(resp)

        print("Status:\n" + resp['status'])
        if resp['status'] == "OK":
            pass
        elif resp['status'] == "NOT_FOUND":
            pass

        print("Gesamtentfernung:\n %i m" % resp['routes'][0]['legs'][0]['distance']['value'])

        print("Gesamtdauer:\n %i sec" % resp['routes'][0]['legs'][0]['duration']['value'])

        route = resp['routes'][0]['legs'][0]['steps']

        for step in route:
            print(step['html_instructions'])


if __name__ == '__main__':
    start, ziel = ("Wien", "Graz")
    rest = Verbindung()

    rest.get_google_driving_api("origin=" + start + "&destination=" + ziel + "&language=de&sensor=false")
