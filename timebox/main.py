import sys
import esp32
from neopixel import NeoPixel
from machine import *
from time import *
from lib.helper import *

# Teil 1: LEDs

# Aufgabe 1: Farben definieren
#
# Die Farben der LEDs im Ring werden als RGB Wert angeben.
# RGB steht für Rot, Grün, Blau.
# Mit diesen drei Farben können alle anderen gemischt werden.
# Definiere einige Farben indem du einer Variablen zuweist welche Anteile der drei Grundfarben
# du kombinieren möchtest.
# Dabei bedeutet 0 aus und 255 die maximale Helligkeit der Farbe.
# Achtung die LEDs sind sehr hell!
#
# Beispiel:
red = (255, 0, 0)
lila = (10, 0, 10)  # Lila setzt sich aus gleichen Anteilen von rot und blau zusammen.

# TODO (Aufgabe 1): Definiere hier weitere Farben!


# Aufgabe 2: Farben anzeigen
#
# Damit die Farben auch auf dem Ring angezeigt werden, schreiben wir eine Funktion,
# die uns dabei hilft.
# Der Ring hat 12 LEDs, die unabhängig von einander gesteuert werden können.
# Dazu muss angegeben werden, welche LED in welcher Farbe leuchten soll.
# Der Code dazu sagt aus, setze das Pixel an der Stelle [Nummer] auf den Wert der Farbe.
# number und color sind dabei Funktionsargumente. Wenn wir die Funktion später
# nutzen, um die LEDs leuchten zu lassen, schreiben wir zum Beispiel:
#
# set_pixel(0, red)
#
# Achtung: Informatiker zählen immer ab 0 - das ist die erste LED!
# Erst wenn auch die Funktion pixel.write() aufgerufen wird, ändert sich die Farbe!
# Ergänze die fehlende Anweisung!
def set_pixel(number, color):
    pixel[number] = color
    # pixel.write() # TODO (Aufgabe 2): Kommentiere die Zeile aus, um die LEDs auch leuchten zu lassen


# Testzeit!
#
# Rufe nun set_pixel(number, color) für verschiedene Pixel im Ring und deine
# vorher definierten Farben in der Methode setup() auf.

# Diese Funktion wird exakt einmal beim Start des Mikrocontollers ausgeführt.
# Hier steht alles, was zu Beginn eingerichtet werden muss.
def setup():
    global rtc
    global pixel

    rtc = RTC()
    pin = Pin(16, Pin.OUT)
    pixel = NeoPixel(pin, 12)

    connect_to_wlan("inovexgast", "in0vexGast")
    set_exact_time(rtc)

    # TODO (Aufgabe 2): Lass deine Farbe aufleuchten
    #  - Nutze die Funktion set_pixel(number, color) hier, um LEDs direkt beim
    #    Start des Mikrocontrollers leuchten zu lassen!
    #  - Teste den Code


# Aufgabe 3: LEDs ausschalten
#
# Manchmal sollen die LEDs aber ja auch wieder ausgehen... alle.
# Definiere zuerst oben eine "Farbe" für aus!
#
# Natürlich könnte man jetzt mit set_pixel(number, color) jede LED einzeln ausschalten.
# Aber Informatiker sind ziemlich faul und schreiben nicht gerne so viel ähnlichen Code.
# Wir nutzen dazu Schleifen!
# For-Schleifen erledigen einen Ablauf genau so oft wie gewünscht.
# Die Zählvariable i gibt an, im wie vielten Durchlauf der Schleife wir uns befinden.
#
# Beispiel:
# for i in range(5):
#     # tut etwas
#
# Die obige Schleife führt alles, was eingerückt bei "tut etwas" steht, genau 5 mal aus.
#
# Schreibe den fehlenden Code, damit alle 12 LEDs ausgeschaltet werden!
def clear_pixels():
    for i in range():  # TODO (Aufgabe 3): Lasse die Schleife 12 mal ausführen
        pixel[i] = ()  # TODO (Aufgabe 3): Setze das Tupel (0, 0, 0) als Farbdefinition

    pixel.write()


# Testzeit!
#
# Suche weiter unten in der Datei die Funktion loop() und rufe von dort
# set_pixel(number, color) und clear_pixels() auf, um die LEDs in verschiedenen
# Farben leuchten und blinken zu lassen!


# Teil 2: Uhr
#
# Aufgabe 4:
#
# Mit dem was wir über den LED Ring gelernt haben lassen sich nun praktische Dinge
# bauen - zum Beispiel eine Uhr.
#
# Der Mikrocontroller ESP32 hat sowohl WLAN als auch eine sogenannte Echtzeituhr.
# Über WLAN kann der ESP32 initial einmal bei einer sehr genauen Zeitquelle im
# Internet die exakte Uhrzeit (und das Datum) erfragen.
# Durch die Echtzeituhr ist er in der Lage die Zeit genau weiter zu zählen, selbst
# wenn für einige Zeit nicht die Zeitquelle nicht verfügbar sein sollte.
# Perfekt für unsere eigene Uhr!
#
# Um die exakte Zeit zu erfragen und der Echtzeituhr mitzuteilen, musst du nichts
# weiter tun - Das wird schon in der setup-Funktion
# durch den Aufruf von set_exact_time(rtc) erledigt.
#
#
# Testzeit!
#
# Aber wie sieht die Zeit eigentlich jetzt im Mikrocontroller aus?
# Schreibe
#
#       current_time = rtc.datetime()
#
# in die Loop-Funktion, um die aktuelle Uhrzeit in jedem Schleifendurchlauf in die
# Variable current_time (du kannst sie auch anders nennen, wenn das einfacher für dich ist)
# zu speichern.
# Damit du nun auch etwas siehst, schreibe
#
#       print(current_time)
#
# in die Zeile danach und öffne mit einem Klick auf "Terminal" die Textausgabe des ESP32.
#
# Finde heraus was die Zahlen in der Ausgabe bedeuten!
# Lösung: (year, month, day, weekday, hours, minutes, seconds, subseconds)


# Aufgabe 5:
#
# Nun wollen wir die Zeit auf dem Pixelring darstellen - überlege, welche Möglichkeiten
# es mit den 12 Pixeln dafür gibt.
# Wenn deine Idee von der Lösung hier abweicht, kannst du später noch eine eigene
# Variante bauen oder diese hier verfeinern!
# Deine Kreativität hat hier keine Grenzen.
#
#
# Eine erste und einfache Idee ist es, sich an einer klassischen Uhr zu orientieren.
# Auf der sind ebenfalls die Zahlen von 1 - 12 (also passend zu unseren 12 Pixeln) dargestellt.
# Stunden, Minuten und Sekundenzeiger können zum Beispiel durch verschiedene Farben realisiert werden.
# Was soll passieren, wenn die Zeiger übereinander stehen?
# Wie könnte man damit umgehen, dass im Gegensatz zu einer normalen Uhr keine "Minutenpixel" verfügbar sind?
#
#  1. Stunde setzen
#
# Eigentlich ist es ganz einfach die Stunde anzuzeigen. Genau wie bei einer normalen Uhr.
# Wir haben 12 Pixel für 2 mal 12 Stunden - Vormittags und Nachmittags, am und pm, wie auch im Englischen.
# Die Stunde wird aber im 24h Format dargestellt.
# Also was ist zu tun?
#
# WENN die Stunde > 11 ist
#   ist die (neue) Stunde = die (alte) Stunde - 12
#
# Dann musst du nur noch für die Stunde das entsprechende Pixel setzen.
# Das geht wie zuvor, nur dass du als Index, welches Pixel du anschalten willst, jetzt einfach die
# Variable hour nutzen kannst.
#
# Such dir eine Farbe aus und schreibe die Logik für die Stunde als Programmcode in die Funktion
# set_time(hour, minute, second)!
#
#
# Testzeit!
#
# Rufe die Funktion set_time(hour, minute, second) in der Loop-Funktion auf!
# Dazu musst du dich kurz an die letzte Aufgabe erinnern.
# Wir hatten die aktuelle Uhrzeit in der Variablen current_time gespeichert und du hast dir überlegt,
# welche der ausgegebenen Zahlen was bedeutet.
# Aktuell interessieren wir uns nur für die Stunde, die Minute und die Sekunde.
# Einen einzelnen Wert aus dem gesamten Gebilde current_time können wir durch folgende Zeile erhalten
#
#   wert = current_time[index]
#
# Dabei ist der Index der x. Wert von links gezählt (Informatiker zählen immer noch ab 0!)
#
# Rufe nun die Funktion set_time mit den extrahierten Werten auf!
#
#   set_time(hour, minute, second)
#


def set_time(hour, minute, second):
    # TODO (Aufgabe 5, optional): Passe die Zeitzone mit der Variable hour an
    # hour = hour + 2  # fix time zone

    # TODO (Aufgabe 5): Schreibe die Logik für die Stunde, indem du 24 Stunden mittels 12 Pixel darstellst
    # if hour > 11:
    #     hour = hour - 12

    minute = int(minute / 5)
    second = int(second / 5)
    print("hour:")
    print(hour)
    print("minute:")
    print(minute)

    # TODO (Aufgabe 5): Setze den Pixel für die Stundenangabe analog zu der Minute und der Sekunde
    # pixel[hour] = (10, 0, 0)
    # TODO (Aufgabe 5): Teste den Code nun weiter unten in loop()

    pixel[minute] = (0, 10, 0)
    pixel[second] = (0, 0, 10)

    if second == minute:
        pixel[minute] = (0, 10, 10)

    if second == hour:
        pixel[hour] = (10, 0, 10)

    if minute == hour:
        pixel[hour] = (10, 10, 0)
        if second == minute:
            pixel[hour] = (10, 10, 10)

    pixel.write()


def loop():
    while True:
        # TODO (Aufgabe 3): Lasse die LEDs in verschiedenen Farben leuchten
        #  - Rufe dafür set_pixel(number, color) und clear_pixels() auf, um die LEDs in verschiedenen
        #    Farben leuchten und blinken zu lassen!
        #  - Teste den Code
        #  Achtung:
        #  Die Funktion loop() wird in einer ewigen Schleife ausgeführt!
        #  Um einen Effekt zu sehen, muss zwischen den einzelnen Anweisungen etwas Zeit vergehen.
        #  Nutze sleep(3) um das An- und Ausschalten zu verzögern!
        #  Was passiert, wenn du sleep(10) schreibst?

        # TODO (Aufgabe 4): Frage die Uhrzeit ab
        #  - Speichere die jetzige Uhrzeit in einer Variable namens current_time
        #  - Schreibe die Variable ins Log aus
        # current_time = rtc.datetime()
        # print(current_time)

        # TODO (Aufgabe 5): Setze die Zeit
        #  - Setze die Zeit mit der jetzigen Uhrzeit, die du vorher gespeichert hast
        #  - Teste den Code
        # clear_pixels()
        # set_time(current_time[4], current_time[5], current_time[6])
        print("schlafe")  # TODO: Lösche die Zeile nach dem Testen
        sleep(3)


# Hier brauchst du nichts machen,
# diese Funktionen starten das Programm auf dem Mikrocontroller!
def main():
    setup()
    loop()


if __name__ == "__main__":
    sys.exit(main())
