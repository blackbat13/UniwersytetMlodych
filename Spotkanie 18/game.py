import pgzrun
import random
import socket

WIDTH = 500
HEIGHT = 500
GRID_SIZE = 10
CELL_WIDTH = WIDTH // GRID_SIZE
CELL_HEIGHT = HEIGHT // GRID_SIZE

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
"""
1 - red
2 - green
3 - blue
4 - yellow
5 - magenta
6 - cyan
"""

board = []
player_pos = [(0, GRID_SIZE - 1), (GRID_SIZE - 1, 0)]  # Współrzędne graczy
player_id = 0  # Numer naszego gracza
opponent_id = 1  # Numer przeciwnika

# Inicjalizacja połączenia z serwerem
server = "127.0.0.1"  # Adres IP serwera
port = 5555
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((server, port))  # Lączymy się z serwerem
player_id = int(connection.recv(2048).decode())  # Otrzymujemy od serwera swój numer gracza
opponent_id = (player_id + 1) % 2  # Obliczamy id przeciwnika
print("Numer gracza:", player_id)

seed = int(connection.recv(2048).decode())  # Otrzymujemy ziarno od serwera
random.seed(seed)

current_player = 0  # Mówi nam, czyja jest teraz tura

connection.setblocking(False)  # Ustawiamy socket (gniazdo) w tryb nie blokowania


# LINK: https://tiny.pl/773sc


def on_key_down(key):  # Obsługa klawiatury - ruch gracza
    global current_player

    if current_player != player_id:  # Jeżeli to nie jest nasza tura, to nie obsługuj klawiatury
        return
    x, y = player_pos[player_id]  # Odczytujemy współrzędne naszego gracza
    old_color = board[x][y]

    x2, y2 = player_pos[opponent_id]  # Pozycja przeciwnika
    opp_color = board[x2][y2]  # Kolor przeciwnika

    if key == keys.K_1 and old_color != 0 and opp_color != 0:
        change_color(x, y, old_color, 0)
        connection.send(str.encode("0"))  # Wysyłamy ruch na serwer
        current_player = (current_player + 1) % 2  # Zmieniamy turę gracza
    if key == keys.K_2 and old_color != 1 and opp_color != 1:
        change_color(x, y, old_color, 1)
        connection.send(str.encode("1"))  # Wysyłamy ruch na serwer
        current_player = (current_player + 1) % 2  # Zmieniamy turę gracza
    if key == keys.K_3 and old_color != 2 and opp_color != 2:
        change_color(x, y, old_color, 2)
        connection.send(str.encode("2"))  # Wysyłamy ruch na serwer
        current_player = (current_player + 1) % 2  # Zmieniamy turę gracza
    if key == keys.K_4 and old_color != 3 and opp_color != 3:
        change_color(x, y, old_color, 3)
        connection.send(str.encode("3"))  # Wysyłamy ruch na serwer
        current_player = (current_player + 1) % 2  # Zmieniamy turę gracza
    if key == keys.K_5 and old_color != 4 and opp_color != 4:
        change_color(x, y, old_color, 4)
        connection.send(str.encode("4"))  # Wysyłamy ruch na serwer
        current_player = (current_player + 1) % 2  # Zmieniamy turę gracza
    if key == keys.K_6 and old_color != 5 and opp_color != 5:
        change_color(x, y, old_color, 5)
        connection.send(str.encode("5"))  # Wysyłamy ruch na serwer
        current_player = (current_player + 1) % 2  # Zmieniamy turę gracza


def change_color(x, y, old_color, new_color):  # Rekurencyjna zmiana kolorów (algorytm flood fill)
    # Po pierwsze sprawdzamy, czy nie wyszliśmy poza planszę
    if x < 0 or y < 0:
        return
    if x >= GRID_SIZE or y >= GRID_SIZE:
        return

    if board[x][y] == old_color:  # Jeżeli to "nasze" pole, czyli ma nasz obecny kolor
        board[x][y] = new_color  # Zmieniamy kolor na nowy
        # Odwiedzamy wszystkich sąsiadów (wywołania rekurencyjne):
        change_color(x + 1, y, old_color, new_color)  # Prawo
        change_color(x - 1, y, old_color, new_color)  # Lewo
        change_color(x, y + 1, old_color, new_color)  # Dół
        change_color(x, y - 1, old_color, new_color)  # Góra


def draw():
    screen.fill((255, 255, 255))
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            place = Rect((x * CELL_WIDTH, y * CELL_HEIGHT), (CELL_WIDTH, CELL_HEIGHT))
            color_number = board[x][y]  # Pobieramy numer koloru z danego pola gry
            place_color = colors[color_number]  # Odczytujemy kolor z listy kolorów
            screen.draw.filled_rect(place, place_color)  # Rysujemy kolorowe pole
            screen.draw.rect(place, (0, 0, 0))


def update():
    global current_player

    if current_player == player_id:  # Jeżeli to nasza tura, to nic nie robimy
        return

    try:
        move = int(connection.recv(2048).decode())  # Odczytujemy ruch przeciwnika
        x, y = player_pos[opponent_id]  # Pobieramy współrzędne przeciwnika
        old_color = board[x][y]  # Pobieramy obecny kolor przeciwnika
        change_color(x, y, old_color, move)  # Zmieniamy kolor przeciwnika
        current_player = (current_player + 1) % 2  # Zmieniamy obecnego gracza
    except:
        pass  # Zignoruj potencjalne błędy


def init_board():
    global board
    board = []
    for x in range(GRID_SIZE):
        board.append([])  # Dodajemy nowy wiersz
        for y in range(GRID_SIZE):
            board[x].append(random.randint(0, len(colors) - 1))  # Dodajemy losowy kolor pola o współrzędnych (x,y)


init_board()  # Inicjalizujemy tablicę gry, przy uruchomieniem gry
pgzrun.go()
