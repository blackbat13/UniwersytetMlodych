import random
import pgzrun

WIDTH = 800
HEIGHT = 600

# Tytuł gry
TITLE = 'Pong'

# Główny kolor elementów gry
kolor = 'yellow'
kolor_tla = (64, 64, 64)

lewa = Actor("lewa.png")
lewa.left = 10
lewa.top = HEIGHT / 2
lewa.wynik = 0

prawa = Actor("prawa.png")
prawa.left = WIDTH - 30
prawa.top = HEIGHT / 2
prawa.wynik = 0

pilka = Actor("pilka.png")
pilka.left = WIDTH / 2
pilka.top = HEIGHT / 2
pilka.px = 5
pilka.py = 5
pilka.koniec_gry = False


def draw():
    screen.fill(kolor_tla)

    if lewa.wynik == 11:
        screen.draw.text(
            "LEWY WYGRYWA!!!",
            color=kolor,
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=96
        )
        pilka.koniec_gry = True
    elif prawa.wynik == 11:
        screen.draw.text(
            "PRAWY WYGRYWA!!!",
            color=kolor,
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=96
        )
        pilka.koniec_gry = True
    else:
        lewa.draw()
        prawa.draw()
        pilka.draw()

    # show the score for the left player
    screen.draw.text(
        "Lewy: " + str(lewa.wynik),
        color=kolor,
        center=(WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # show the score for the right player
    screen.draw.text(
        'Prawy: ' + str(prawa.wynik),
        color=kolor,
        center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # a dividing line
    screen.draw.line(
        (WIDTH / 2, 40),
        (WIDTH / 2, HEIGHT - 40),
        color=kolor)

# Aktualizujemy stan gry - ruchy graczy i piłki
def update():
    ruch_graczy()
    ruch_pilki()


def ruch_graczy():
    if keyboard.up:
        if prawa.top - 5 > 40:
            prawa.top -= 5
    elif keyboard.down:
        if prawa.top + 104 + 5 < HEIGHT - 40:
            prawa.top += 5

    if keyboard.w:
        if lewa.top - 5 > 40:
            lewa.top -= 5
    elif keyboard.s:
        if lewa.top + 104 + 5 < HEIGHT - 40:
            lewa.top += 5


def resetuj_pilke():
    pilka.left = WIDTH // 2
    pilka.top = HEIGHT // 2
    pilka.px = random.choice([-5, 5])
    pilka.py = random.choice([-5, 5])


def ruch_pilki():
    # Przemieszczamy piłkę zgodnie z jej prędkością
    pilka.left += pilka.px
    pilka.top += pilka.py

    # Odbijamy od ścian - góra i dół
    if pilka.top <= 40:
        pilka.py *= -1

    if pilka.top >= HEIGHT - 40:
        pilka.py *= -1

    # Odbijamy od paletek
    if lewa.colliderect(pilka):
        pilka.px *= -1

    if prawa.colliderect(pilka):
        pilka.px *= -1

    if pilka.left <= 0 and not pilka.koniec_gry:
        resetuj_pilke()
        prawa.wynik += 1

    if pilka.left >= WIDTH and not pilka.koniec_gry:
        resetuj_pilke()
        lewa.wynik += 1


pgzrun.go()
