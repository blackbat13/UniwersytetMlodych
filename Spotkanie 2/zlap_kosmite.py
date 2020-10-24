# Złap kosmitę!
# Gra polega na tym, żeby spróbować złapać kosmitę, który porusza się w losowym kierunku.
# Za każde kliknięcie w kosmitę zdobywasz punkt.
# Uwaga! Jak chybisz, to tracisz punkt!
# Z każdym trafieniem kosmita przyspiesza!
# Ile punktów uda Ci się zdobyć?

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Podajemy kolor tła za pomocą trzech wartości, liczb od 0 do 255
# Liczby określają ile każdego z trzech podstawowych kolorów używamy
# Pierwsza liczba to ilość koloru czerwonego (Red)
# Druga liczba to ilość koloru zielonego (Green)
# Trzecia liczba to ilość koloru niebieskiego (Blue)
kolor_tla = (0, 120, 0)

# Tworzymy nową postać, nowego aktora naszej gry, na podstawie grafiki kosmita.png
kosmita = Actor("kosmita.png")

# Ustalamy początkową pozycję naszej postaci na ekranie
# Podajemy dwie współrzędne: x, y
# x oznacza odległość od lewej strony
# y oznacza odległość od góry ekranu
kosmita.pos = (200, 200)

# W zmiennej punkty będziemy zliczać punkty zdobyte przez gracza
kosmita.punkty = 0

# Tutaj zapamiętujemy, jak szybko porusza się kosmita
kosmita.poziom = 2

# Zapamiętujemy prędkość kosmity: poziomą (x) i pionową (y)
kosmita.px = 1
kosmita.py = 0


def draw():
    # Wypełniamy ekran wybranym kolorem
    screen.fill(kolor_tla)

    # Rysujemy kosmitę
    kosmita.draw()

    # Wypisujemy ilość punktów
    screen.draw.text("Punkty: " + str(kosmita.punkty), (50, 30), color="orange")


def update():
    # Przesuwamy kosmitę, zmieniając jego pozycje zgodnie z prędkością i trudnością gry
    kosmita.left += kosmita.px * kosmita.poziom
    kosmita.top += kosmita.py * kosmita.poziom

    # Jeżeli odległość kosmity od lewego brzegu jest większa od szerokości ekranu
    # Czyli, jeżeli kosmita wyszedł poza ekran
    if kosmita.left > WIDTH:
        # Przesuwamy kosmitę na początek
        kosmita.left = 0

    # Jeżeli kosmita wyszedł z lewej strony ekranu, przesuwamy go w prawo
    if kosmita.left < 0:
        kosmita.left = WIDTH

    # Jeżeli kosmita wyszedł z dołu ekranu, przesuwamy go na górę
    if kosmita.top > HEIGHT:
        kosmita.top = 0

    # Jeżeli kosmita wyszedł z góry ekranu, przesuwamy go na dół
    if kosmita.top < 0:
        kosmita.top = HEIGHT


# Tutaj piszemy, co ma się wydarzyć, gdy gracz kliknie myszką
# Zmienna pos zawiera pozycję myszki na ekranie
def on_mouse_down(pos):
    # Jeżeli kliknęliśmy w kosmitę, to
    if kosmita.collidepoint(pos):
        # Zwiększamy ilość punktów
        kosmita.punkty += 1

        # Ustawiamy kosmitę w losowym miejscu
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)

        # Zwiększamy szybkość kosmity, jeżeli nie jest już zbyt szybki
        if kosmita.poziom < 10:
            kosmita.poziom += 1
    else:
        # Jeżeli nie trafiliśmy w kosmitę, odejmujemy punkty
        kosmita.punkty -= 1


pgzrun.go()
