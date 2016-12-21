import pygame, time
from pygame.locals import *
from math import sin, cos, radians
import sys


class Clock_Analog_Digital:
    """
        Clock_Analog_Digital - Klasse

        Die Clock_Analog_Digital-Klasse beinhaltet die Logik der Klasse um eine Analoge oder Digitale Uhr zu erstellen.
        Mit der Taste A wählt man die Analogdarstellung, mit der Taste D wählt man die Digitaldarstellung,
        mit der Taste P wechselt man zwischen kontinuierlicher Variante und diskreter Variante (Analogdarstellung) und
        wenn man escape drückt dann wird die Uhr beendet.

        Als Pattern wird die Strategy-Pattern verwendet.

        __version__ = '1.0'

        __author__ = 'Oezsoy Ahmet'

    """

    def __init__(self, analog_loop=True):
        """
        Konstruktor - dient für die Initialiserung der Attribute und um die Definition der Punkte bzw. Farben.
        Mit welcher Uhr das Programm das gestartet wird, hängt vom Benutzer ab - parameter (Strategy Pattern) analog_loop

        Es gibt 2 Strategien:
        Entweder mit der Analogen Uhr starten (analog_loop=True) oder mit der Digitalen Uhr starten (analog_loop=False)

        :param analog_loop: Wenn es true ist, dann erscheint die Analoge Uhr. Wenn es false ist, dann erscheint die Digitale Uhr.
        """
        # Initialisieren der Farben und des Bildschirms(Bildfläche)
        self.color_white = (255, 255, 255)
        self.color_red = (255, 0 , 0)
        self.color_black = (0, 0, 0)
        self.color_green = (0, 255, 0)
        self.digitBackground = (0, 255, 0)
        self.digitBorder = (0, 0, 0)
        self.field = pygame.display.set_mode((900, 900))
        self.field.fill(self.color_red)
        self.point_x = 450
        self.point_y = 450
        self.center_point = ((self.point_x, self.point_y))
        self.analog_loop = analog_loop
        self.second_jump = True
        pygame.init()

    def punkt(self, r, angle):
        """
        Diese Funktion erstellt ein Punkt mit der Distanz/Radius r und dem Winkel W im Mittelpunkt.

        :param r: radius/distanz zum Mittelpunkt
        :param angle: winkel zum Mittelpunkt
        :return: punkt (x,y)
        """
        w1 = radians(angle * 6 - 90)
        x1 = int(self.point_x + r * cos(w1))
        y1 = int(self.point_y + r * sin(w1))
        return ((x1, y1))

    def analog(self):
        """
        Diese Funktion erstellt eine Analoge Uhr.
        """
        self.field.fill(self.color_white)
        for i in range(60):
            pygame.draw.circle(self.field, self.color_black, self.punkt(430, i), 4)
        for i in range(12):
            pygame.draw.circle(self.field, self.color_black, self.punkt(430, i * 5), 7)
        time_save = time.localtime()
        if self.second_jump:
            s = time_save.tm_sec
        else:
            s = time_save.tm_sec + (time.time() % 1)
        m = time_save.tm_min
        h = time_save.tm_hour
        if h > 12:
            h -= 12
        hm = (h + m / 60.0) * 5
        pygame.draw.circle(self.field, self.color_red, self.center_point, 422)
        pygame.draw.line(self.field, self.color_black, self.center_point, self.punkt(360, hm), 10)
        pygame.draw.line(self.field, self.color_black, self.center_point, self.punkt(410, m), 8)
        pygame.draw.line(self.field, self.color_white, self.center_point, self.punkt(420, s), 4)
        pygame.display.set_caption("ANALOG CLOCK")
        pygame.display.update()

    def digital(self):
        """
        Diese Funktion erstellt eine Digitale Uhr, wo die zeit als text/String erstellt wird mithilfe von pygame.
        """
        zeit = time.localtime()
        p = zeit.tm_sec
        m = zeit.tm_min
        h = zeit.tm_hour
        if (p < 10):
            s = "0" + str(p)
        if (h < 10):
            h = "0" + str(h)
        if (m < 10):
            m = "0" + str(m)
        pygame.draw.rect(self.field, self.digitBorder, (70, 295, 730, 160), 0)
        pygame.draw.rect(self.field, self.digitBackground, (75, 300, 720, 150), 0)
        myfont = pygame.font.SysFont("None", 250)
        label = myfont.render(str(h) + ":" + str(m) + ":" + str(p), 1, self.color_black)
        self.field.blit(label, (75, 300))
        pygame.display.set_caption("DIGITAL CLOCK")
        pygame.display.update()

    def handleAction(self):
        """
        Diese Funktion ist verantwortlich für das Action/Event - Handling.
        Reagiert auf die Tastatureingaben vom Benutzer und führt die jeweiligen Funktionen aus, wie zum Beispiel
        wechseln von Analog zu Digital, wechseln zwischen kontinuierlicher Variante und diskreter Variante(Analogdarstellung)
        und beenden der Uhr.
        """
        while True:
            for event in pygame.event.get():
                if event.type == (pygame.QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    sys.exit(0)
                if event.type == KEYDOWN and event.key == K_d:
                    self.analog_loop = False
                if event.type == KEYDOWN and event.key == K_a:
                    self.analog_loop = True
                if event.type == KEYDOWN and event.key == K_p:
                    if self.second_jump:
                        self.second_jump = False
                    else:
                        self.second_jump = True
            if self.analog_loop:
                self.field.fill(self.color_white)
                self.analog()
            else:
                self.field.fill(self.color_white)
                self.digital()
            pygame.display.update()


if __name__ == '__main__':
    Clock_Analog_Digital(True).handleAction() # Beim erzeugen des Objektes kann man die Vorgehenweise(Strategy) aussuchen. (analog=True, digital=False)