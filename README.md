# TimeBox - Girl's Day 2023

Zum Girl's Day 2023 programmieren und basteln wir unsere eigene Uhr - aus einer Holzbox,
dem Mikrocontroller ESP32 und einem (NeoPixel-)Ring mit 12 LEDs!

## Verkabeln
Der NeoPixel hat 3 Kontakte, die bereits verlötet sind: VCC, GND und IN.
Diese Steckbrücken müssen auf VCC -> 5V, GNC -> GND und IN auf euren ausgewählten GPIO (zB PIN #16) des ESPs gesteckt werden. 

## Vorbereitungen
- Um den Mikrocontroller zu programmieren benötigen wir eine Entwicklungsumgebung und
  müssen diese zuerst installieren. Wir nutzen [Thonny](https://thonny.org/). 
  Auf der Thonny-Webseite findet ihr unter <i><Instructions & downloads></i> Informationen zur Installation.
- Wenn nicht bereits geschehen, muss der Mikrocontroller lernen, dass wir mit der Programmiersprache
  [MicroPython](https://micropython.org/) arbeiten wollen.
  Dazu müssen wir die MicroPython Firmware installieren.
  Gehe dazu in Werkzeuge->Optionen...->Interpreter (Raspi: Extras->Optionen...->Interpreter) und klicke unten rechts auf
  MicroPython installieren oder aktualisieren. Ein Thonny-Neustart ist nach der Installation (des esptool) notwendig ;-)
  Anschließend nochmals zu Interpreter navigieren, wähle den richtigen Port aus und lade die Firmware (entweder von der MicroPython Seite oder aus diesem Repo)
  mit dem Button installieren hoch.


## Programm dauerhaft hochladen
- Hauptdatei muss main.py heißen!
- Rechtsklick -> Upload to /
- Auf ESP32 EN Button drücken
