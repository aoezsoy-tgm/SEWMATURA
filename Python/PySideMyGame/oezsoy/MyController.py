from PySide.QtCore import *
from PySide.QtGui import *
import oezsoy.MyView, oezsoy.MyModel, sys
from random import *

class MyController(QMainWindow):
    """
    Controller:
    Im Controller werden die Methoden von der Model Klasse aufgerufen und es reagiert auf die Button Klicks(Funktion).

    __version__ = '1.0'

    __author__ = 'Oezsoy Ahmet'

    """
    def __init__(self, parent=None):
        """
        Konstruktor zum Initialiseren :
        Es wird ein neues Spiel gestartet und speichert die Buttons in einer Liste.

        :param parent:
        """
        super().__init__(parent)
        self.myForm = oezsoy.MyView.Ui_MainWindow()
        self.myForm.setupUi(self)
        self.myModel = oezsoy.MyModel.MyModel()
        self.buttonListe = [self.myForm.pushButton0,
                            self.myForm.pushButton1,
                            self.myForm.pushButton2,
                            self.myForm.pushButton3,
                            self.myForm.pushButton4,
                            self.myForm.pushButton5,
                            self.myForm.pushButton6,
                            self.myForm.pushButton7,
                            self.myForm.pushButton8,
                            self.myForm.pushButton9,
                            self.myForm.pushButton10,
                            self.myForm.pushButton11,
                            self.myForm.pushButton12,
                            self.myForm.pushButton13,
                            self.myForm.pushButton14]
        self.cbutton()
        self.start()
        self.myForm.spiele.setText(str(self.myModel.spiele))


    def handleb(self):
        """
        Zuerst wird geschaut ob es sich um einen QPushButton handelt und dann wird der Text vom Button geholt und
        mit den Werten verglichen. (Werte 1-15)
        """
        sender = self.sender()
        if isinstance(sender, QPushButton):
            value = int(sender.text())
        if self.actValue == int(value):
            sender.setEnabled(False)
            self.myModel.cright()
            if self.actValue == 15:
                popup=QMessageBox()
                popup.setText("Gewonnen!")
                popup.setWindowTitle("Gratulations")
                popup.exec_()
            self.myForm.korrekt.setText(str(self.myModel.korrekt))
            self.myForm.gesamt.setText(str(self.myModel.gesamt))
            self.myForm.offen.setText(str(self.myModel.offen))
            self.actValue+=1
        else:
            self.myModel.cwrong()
            self.myForm.falsch.setText(str(self.myModel.falsch))
            self.myForm.gesamt.setText(str(self.myModel.gesamt))


    def cbutton(self):
        """
        Diese Methode ist dafür da, welche Methode bei einem Klick aufgerufen werden soll mithilfe eines ButtonHandlers
        """
        for button in self.buttonListe:
            button.clicked.connect(self.handleb)
        self.myForm.neu.clicked.connect(self.anew)


    def randombutton(self):
        """
        Bei dieser Methode werden die Button durcheinander gemischt damit bei jedem Start neue Zahlen mit einer
        anderen Reihenfolge erscheinen.
        """
        counter = 1
        shuffle(self.buttonListe)
        for buttons in self.buttonListe:
            buttons.setEnabled(True)
            buttons.setText(str(counter))
            counter+=1
        self.actValue=1
        self.myForm.offen.setText(str(self.myModel.offen))


    def anew(self):
        """
        Bei dieser Methode wird die diese Methode aufgerufen wenn der Button 'Neu' Button geklickt wird und
        die Zaehler werden auf Start-Zustand gesetzt.
        """
        self.myModel.newGame()
        self.randombutton()
        self.myForm.korrekt.setText(str(self.myModel.korrekt))
        self.myForm.gesamt.setText(str(self.myModel.gesamt))
        self.myForm.offen.setText(str(self.myModel.offen))
        self.myForm.falsch.setText(str(self.myModel.falsch))
        self.myForm.spiele.setText(str(self.myModel.spiele))


    def start(self):
        """
        @param self
        Wenn ein neues Spiel gestartet wird, werden die Buttons wieder aktiviert und die Zaehler zurückgesetzt.
        """
        self.randombutton()
        self.myModel.newGame()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())