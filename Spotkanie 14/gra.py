import pgzrun
import random

# Szerokość okna
WIDTH = 800

# Wysokość okna
HEIGHT = 600

# Długość boku pojedyńczego, kwadratowego pola
field_size = 20

# Szerokość całego pola gry - ilość pojedyńczych pól
field_width = WIDTH // field_size

# Wysokość całego pola gry - ilość pojedyńczych pól
field_height = HEIGHT // field_size

# Pole gry
field = []

# Dostępne kolory pól gry. Pierwszy jest zarezerwowany na kolor początkowy.
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Ilość dostępnych kolorów
colors_size = len(colors)

# Początkowo gracze mają pierwszy kolor z tablicy
player_color = 0
computer_color = 0

# Zaczyna gracz
current_player = 1


def draw():
    # Czyścimy ekran gry, wypełniając go czarnym kolorem
    screen.fill((0, 0, 0))

    # Rysujemy pole gry
    draw_field()


# Rysowanie pola gry
def draw_field():
    for x in range(field_width):
        for y in range(field_height):
            # Pobieramy kolor pola gry
            field_color = field[x][y]

            # Obliczamy współrzędne pola na ekranie
            field_x = x * field_size
            field_y = y * field_size

            # Tworzymy prostokąt pola gry do narysowania
            field_rect = Rect((field_x, field_y), (field_size, field_size))

            # Rysujemy pole gry na ekranie
            screen.draw.rect(field_rect, field_color)


def update():
    global current_player
    # Jeżeli jest tura komputera
    if current_player == 2:
        # Wykonujemy ruch komputera
        computer_move()
        current_player = 1


# Wykonujemy ruch komputera
def computer_move():
    global computer_color

    new_color = computer_color

    # Dopóki wylosowany ruch nie jest dozwolony
    while new_color == computer_color or new_color == player_color:
        # Losujemy nowy ruch
        new_color = random.randint(1, colors_size - 1)

    flood_fill(field_width - 1, field_height - 1, computer_color, new_color)
    computer_color = new_color


# Odczytujemy ruch gracza
def on_key_down(key):
    global player_color, current_player

    # Jeżeli nie jest tura gracza
    if current_player != 1:
        # Kończymy działanie funkcji
        return

    new_color = player_color
    if key == keys.K_1:
        new_color = 1

    if key == keys.K_2:
        new_color = 2

    if key == keys.K_3:
        new_color = 3

    if key == keys.K_4:
        new_color = 4

    if key == keys.K_5:
        new_color = 5

    # Jeżeli ruch nie jest dozwolony
    if new_color == player_color or new_color == computer_color:
        return

    flood_fill(0, 0, player_color, new_color)
    player_color = new_color
    current_player = 2


def flood_fill(x, y, old_color, new_color):
    global field

    if x < 0 or x >= field_width:
        return

    if y < 0 or y >= field_height:
        return

    if field[x][y] != colors[old_color]:
        return

    field[x][y] = colors[new_color]
    flood_fill(x + 1, y, old_color, new_color)
    flood_fill(x - 1, y, old_color, new_color)
    flood_fill(x, y + 1, old_color, new_color)
    flood_fill(x, y - 1, old_color, new_color)


# Przygotowanie pola gry, wypełniamy je losowymi wartościami
def prepare_field():
    for x in range(field_width):
        # Dodajemy pusty wiersz
        field.append([])

        for y in range(field_height):
            # Losujemy numer koloru, pomijając pierwszy z tablicy
            random_index = random.randint(1, colors_size - 1)

            # Wybieramy kolor, zgodnie z wylosowaną liczbą
            random_color = colors[random_index]

            # Dodajemy nowe pole do planszy
            field[x].append(random_color)

    # Ustawiamy początkowe kolory dla początkowych pól graczy
    field[0][0] = colors[0]
    field[field_width - 1][field_height - 1] = colors[0]


# Przygotowujemy pole gry
prepare_field()

# Uruchamiamy grę
pgzrun.go()
