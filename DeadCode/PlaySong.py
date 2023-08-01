from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, Speaker
from pybricks.media.ev3dev import Image, SoundFile
from pybricks.parameters import Button
from pybricks.tools import wait

ev3 = EV3Brick()
speaker = Speaker()


NOTE_C4 = 261.63
NOTE_D4 = 293.66
NOTE_E4 = 329.63
NOTE_F4 = 349.23
NOTE_G4 = 392.00
NOTE_A4 = 440.00
NOTE_B4 = 493.88

EIGHTH = 250
QUARTER = 500
HALF = 1000

mario_music = [
    (NOTE_E4, EIGHTH),
    (NOTE_E4, EIGHTH),
    (NOTE_E4, EIGHTH),
    (NOTE_C4, EIGHTH),
    (NOTE_E4, EIGHTH),
    (NOTE_G4, QUARTER),
    (NOTE_G3, QUARTER),
    (NOTE_C4, QUARTER),
    (NOTE_G3, QUARTER),
    (NOTE_E3, QUARTER),
    (NOTE_A3, HALF),
    (NOTE_B3, EIGHTH),
    (NOTE_B3, EIGHTH),
    (NOTE_A3, EIGHTH),
    (NOTE_G3, EIGHTH),
    (NOTE_E4, EIGHTH),
    (NOTE_G4, QUARTER),
    (NOTE_A4, EIGHTH),
    (NOTE_F4, EIGHTH),
    (NOTE_G4, EIGHTH),
    (NOTE_E4, EIGHTH),
    (NOTE_C4, EIGHTH),
    (NOTE_D4, QUARTER),
    (NOTE_B3, EIGHTH),
    (NOTE_C4, EIGHTH),
    (NOTE_G3, EIGHTH),
    (NOTE_E3, EIGHTH),
    (NOTE_A3, HALF),
]

def tocar():
    for note in mario_music:
        frequency, duration = note
        speaker.play_notes([(frequency, duration)])

tocar()
