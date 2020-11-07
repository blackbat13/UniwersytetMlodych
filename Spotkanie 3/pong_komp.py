import random
import pgzrun

WIDTH = 800
HEIGHT = 600

# Tytuł gry
TITLE = 'Pong'

# Główny kolor elementów gry
kolor = 'yellow'
kolor_tla = (64, 64, 64)

# Tworzymy aktorów - lewą paletkę, prawą paletkę i piłkę
# Paletki mają początkową pozycję i wynik
lewa = Actor("lewa.png")
lewa.left = 10
lewa.top = HEIGHT / 2
lewa.wynik = 0

prawa = Actor("prawa.png")
prawa.right = WIDTH - 10
prawa.top = HEIGHT / 2
prawa.wynik = 0

# Piłka ma jeszcze określoną prędkość poruszania się
# A także informację o tym, czy gra została zakończona
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

    # Wypisujemy wynik lewego gracza
    screen.draw.text(
        "Lewy: " + str(lewa.wynik),
        color=kolor,
        center=(WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # Wypisujemy wynik prawego gracza
    screen.draw.text(
        'Prawy: ' + str(prawa.wynik),
        color=kolor,
        center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # Eysujemy linię dzielącą pole gry
    screen.draw.line(
        (WIDTH / 2, 40),
        (WIDTH / 2, HEIGHT - 40),
        color=kolor)


# Aktualizujemy stan gry - ruchy graczy i piłki
def update():
    # Jeżeli gra nie została jeszcze zakończona
    if not pilka.koniec_gry:
        # Odczytujemy ruchy graczy
        ruch_graczy()

        # Poruszamy piłkę
        ruch_pilki()


# Odczytujemy ruchy graczy
def ruch_graczy():
    # Prawy gracz porusza się za pomocą strzałek góra i dół
    if keyboard.up:
        if prawa.top - 5 > 40:
            prawa.top -= 5
    elif keyboard.down:
        if prawa.bottom + 5 < HEIGHT - 40:
            prawa.top += 5

    # Lewy gracz porusza się automatycznie
    if lewa.y > pilka.y:
        if lewa.top - 5 > 40:
            lewa.top -= 5
    elif lewa.y < pilka.y:
        if lewa.bottom + 5 < HEIGHT - 40:
            lewa.top += 5


# Resetujemy pozycję piłki
def resetuj_pilke():
    pilka.left = WIDTH // 2
    pilka.top = HEIGHT // 2
    pilka.px = random.choice([-5, 5])
    pilka.py = random.choice([-5, 5])


# Obliczamy ruch piłki i ją przemieszczamy
def ruch_pilki():
    # Przemieszczamy piłkę zgodnie z jej prędkością
    pilka.left += pilka.px
    pilka.top += pilka.py

    # Odbijamy od ścian - góra i dół
    if pilka.top <= 40:
        pilka.py *= -1

    if pilka.bottom >= HEIGHT - 40:
        pilka.py *= -1

    # Odbijamy od paletek
    if lewa.colliderect(pilka):
        pilka.px *= -1

    if prawa.colliderect(pilka):
        pilka.px *= -1

    # Jeżeli piłka wypadła poza ekran, to jeden z graczy dostaje punkt
    if pilka.left <= 0:
        resetuj_pilke()
        prawa.wynik += 1

    if pilka.right >= WIDTH:
        resetuj_pilke()
        lewa.wynik += 1


pgzrun.go()
