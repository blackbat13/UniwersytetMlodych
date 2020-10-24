import pgzrun

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


def draw():
    # Wypełniamy ekran wybranym kolorem
    screen.fill(kolor_tla)

    # Rysujemy kosmitę
    kosmita.draw()


def update():
    # Przesuwamy kosmitę w prawo, zwiększając jego odległość od lewej strony ekranu
    kosmita.left += 2

    # Jeżeli odległość kosmity od lewego brzegu jest większa od szerokości ekranu
    # Czyli, jeżeli kosmita wyszedł poza ekran
    if kosmita.left > WIDTH:
        # Przesuwamy kosmitę na początek
        kosmita.left = 0


# Tutaj piszemy, co ma się wydarzyć, gdy gracz kliknie myszką
def on_mouse_down():
    kosmita.top += 2


pgzrun.go()
