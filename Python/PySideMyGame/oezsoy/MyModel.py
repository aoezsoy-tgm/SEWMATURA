class MyModel(object):
    """
    Model
    Kümmert sich um die Statistik(Logik).

    __version__ = '1.0'

    __author__ = 'Oezsoy Ahmet'

    """
    def __init__(self):
        """
        Konstruktor:
        Dient zum Initialisieren der Variablen
        """
        self.falsch = 0
        self.gesamt = 0
        self.spiele = 0
        self.offen = 15
        self.korrekt = 0


    def cright(self):
        """
        Bei einem richtigen Klick wird diese Methode aufgerufen.
        """
        self.korrekt +=1
        self.offen -= 1
        self.gesamt += 1


    def cwrong(self):
        """
        Bei einem falschen Klick wird diese Methode aufgerufen.
        """
        self.falsch +=1
        self.gesamt +=1


    def newGame(self):
        """
        Beim Neustart wird diese Methode aufgerufen. (Alle Variablen werden zurückgesetzt)
        """
        self.gesamt = 0
        self.spiele += 1
        self.offen = 15
        self.korrekt = 0
        self.falsch = 0
