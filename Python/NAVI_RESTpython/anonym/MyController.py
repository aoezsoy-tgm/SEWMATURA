from PySide.QtCore import *
from PySide.QtGui import *
import anonym.MyView, anonym.MyModel, sys
from random import *

class MyController(QMainWindow):
    """
    Controller

    Die Controller Klasse beinhaltet die Action Listener und ruft die jeweiligen Methoden in der Model Klasse auf, wenn
    die Buttons geklickt werden.

    __version__ = '1.0'

    __author__ = 'Anonym'

    """
    def __init__(self, parent=None):
        """
        Konstruktor zum Initialiseren:

        Erhaelt View und Model als Attribut
        Connected den Anzeigen Button mit der dazugehoerigen Methode

        :param parent:
        """
        super().__init__(parent)
        self.myForm = anonym.MyView.Ui_MainWindow()
        self.myForm.setupUi(self)
        self.myModel = anonym.MyModel.MyModel()
        self.myForm.submitbutt.clicked.connect(self.submitRequest)

    def submitRequest(self):
        """
        Diese Funktion wird beim Klicken des Anzeigen Buttons aufgerufen.
        Dabei wird zuerst ueberprueft, ob sich in den beiden Eingabefeldern (Start, Ziel) ein Text befindet.
        Sollte kein Text vorhanden sein, wird die Methode im Model nicht aufgerufen.

        Wenn ein Text in den Feldern vorhanden ist, wird die Request Funktion im Model mit den beiden
        Parametern (Start, Ziel) aufgerufen.
        """
        if (self.myForm.startinp.text() == "" or self.myForm.zielin.text()== ""):
            self.myForm.statbar.showMessage("Gültige Adresse eintragen bitte!")
            self.myForm.ausgabe.setText(("Gültige Adresse eintragen bitte!"))
        else:
            start=self.myForm.startinp.text()
            ziel= self.myForm.zielin.text()
            self.myForm.ausgabe.setText(self.myModel.getRequest(start,ziel))
            self.myForm.statbar.showMessage(self.myModel.status_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
