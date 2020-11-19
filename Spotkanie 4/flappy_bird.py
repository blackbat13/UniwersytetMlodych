import pgzrun
import random

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 700

grawitacja = 0.3

ptak = Actor("ptak1", (75, 200))
ptak.py = 0
ptak.martwy = False
ptak.wynik = 0

rura_gora = Actor("gora", anchor=("left", "bottom"))
rura_dol = Actor("dol", anchor=("left", "top"))


def draw():
    screen.blit("tlo", (0, 0))
    rura_gora.draw()
    rura_dol.draw()
    ptak.draw()
    screen.draw.text(str(ptak.wynik), midtop=(WIDTH // 2, 10), fontsize=70)


def update():
    ptak.py += grawitacja
    ptak.y += ptak.py
    if not ptak.martwy:
        rura_gora.left -= 3
        rura_dol.left -= 3

    if not ptak.martwy:
        if ptak.py < 0:
            ptak.image = "ptak2"
        else:
            ptak.image = "ptak1"

    if rura_gora.x < -100:
        ustaw_rury()
        if not ptak.martwy:
            ptak.wynik += 1

    if ptak.colliderect(rura_gora) or ptak.colliderect(rura_dol):
        ptak.image = "martwy"
        ptak.martwy = True
        ptak.angle = -90

    if ptak.y > HEIGHT or ptak.y < 0:
        ptak.y = 200
        ptak.martwy = False
        ptak.wynik = 0
        ptak.py = 0
        ptak.image = "ptak1"
        ustaw_rury()


def on_key_down():
    if not ptak.martwy:
        ptak.py = -7


# Ustawiamy kolejne rury
def ustaw_rury():
    przerwa = random.randint(200, 500)
    rura_gora.pos = (WIDTH, przerwa - 70)
    rura_dol.pos = (WIDTH, przerwa + 70)


ustaw_rury()
pgzrun.go()
