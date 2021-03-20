import pgzrun
import random

WIDTH = 800
HEIGHT = 800

kolory = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)]

kolor_tla = 0

kolo = [1, 2, 3, 4]


def draw():
    screen.fill(kolory[kolor_tla])

    promien = 100
    for numer in kolo:
        kolor = kolory[numer]
        screen.draw.filled_circle((WIDTH / 2, HEIGHT / 2), promien, kolor)
        promien -= 20


def update():
    pass


def on_key_down(key):
    global kolor_tla
    if key == keys.K_1:
        kolor_tla = 1
    if key == keys.K_2:
        kolor_tla = 2
    if key == keys.K_3:
        kolor_tla = 3
    if key == keys.K_4:
        kolor_tla = 4

    if len(kolo) > 0 and kolo[0] == kolor_tla:
        kolo.pop(0)


pgzrun.go()
