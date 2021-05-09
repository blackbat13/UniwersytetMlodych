import pgzrun

WIDTH = 800
HEIGHT = 1000

# Tutaj definiujemy liczbę wierszy i kolumn
rows = 2
columns = 5

# Definiujemy marginesy (odstępy) pomiędzy polami gry
margin = 10

# Lsita do zapamiętania pól gry
fields = []


def draw():
    # Wypełniamy tło białym kolorem
    screen.fill("white")
    # Rysujemy pola gry
    draw_fields()


# Funkcja rysująca pola gry
def draw_fields():
    # Przechodzimy przez wszystkie wiersze
    for row in fields:
        # I przez wszystkie elementy w wierszu
        for el in row:
            # Każdy element rysujemy jako czerwony prostokąt
            screen.draw.filled_rect(el, "red")


# Funkcja wywoływana po kliknięciu myszą
def on_mouse_down(pos):
    # Przechodzimy przez każdy wiersz
    for r in range(len(fields)):
        # I przez każdą kolumnę w wierszu
        for c in range(len(fields[r])):
            # Sprawdzamy, czy gracz kliknął w pole w wierszu r i kolumnie c
            if fields[r][c].collidepoint(pos):
                # Jeżeli tak, to usuwamy wskazane pole i wszystkie przed nim z lewej strony w danym wierszu
                remove_field(r, c)
                # A następnie kończymy sprawdzanie
                return


# Funkcja usuwająca wskazane pole i wszystkie znajdujące się przed nim w danym wierszu
def remove_field(r, c):
    # Dla każdego pola we wskazanym wierszu, od lewej do klikniętego pola
    for i in range(c + 1):
        # Usuwamy pole z początku wiersza
        fields[r].pop(0)


# Funkcja generująca pola gry
def generate_fields():
    # Obliczamy wysokość i szerokość jednego pola, biorąc pod uwagę liczbę wierszy i wysokość okna
    rect_height = (HEIGHT - (rows * margin)) / rows
    rect_width = (WIDTH - (columns * margin)) / columns
    # Dla każdego wiersza
    for r in range(rows):
        # Dodajemy pustą listę do naszej listy pól - pusty wiersz
        fields.append([])
        # Dla każdej kolumny
        for c in range(columns):
            # Tworzymy nowe pole gry - prostokąt umieszczony w wierszu r i kolumnie c
            rect = Rect((rect_width + margin) * c, (rect_height + margin) * r, rect_width, rect_height)
            # Dodajemy nowy prostokąt do obecnego wiersza
            fields[r].append(rect)


# Przed startem gry generujemy planszę
generate_fields()
# Uruchamiamy grę
pgzrun.go()
