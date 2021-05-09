import pgzrun
import socket
import ast

WIDTH = 800
HEIGHT = 1000

fields = []

server = "188.47.52.219"  # Adres IP serwera
port = 35999
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((server, port))  # Lączymy się z serwerem
order = int(connection.recv(2048).decode())

rows, columns = ast.literal_eval(connection.recv(2048).decode())

connection.setblocking(
    False)  # Ustawiamy gniazdo w trybie nieblokowania, tak żaby gra się nie zawieszała podczas czekania na wiadomość od serwera

fields_count = rows * columns

win = 0


def draw():
    global order

    screen.fill("white")
    for row in fields:
        for el in row:
            screen.draw.filled_rect(el, "red")

    if order == 1:
        screen.draw.text("Your turn", center=(WIDTH / 2, 50), color="black")
    else:
        screen.draw.text("Opponent turn", center=(WIDTH / 2, 50), color="black")

    if win == 1:
        screen.draw.text("You Win!", center=(WIDTH / 2, HEIGHT / 2), color="red", fontsize=50)
    elif win == 2:
        screen.draw.text("You Lose!", center=(WIDTH / 2, HEIGHT / 2), color="red", fontsize=50)


def update():
    global order, win
    if order == 2:
        try:
            row, column = ast.literal_eval(connection.recv(2048).decode())
            remove_field(row, column)
            order = 1

            if fields_count == 0:
                win = 2
        except:
            pass


def on_mouse_down(pos):
    global order, win

    if order == 2:
        return

    for r in range(len(fields)):
        for c in range(len(fields[r])):
            if fields[r][c].collidepoint(pos):
                remove_field(r, c)
                move = str((r, c))
                connection.send(str.encode(move))
                order = 2
                if fields_count == 0:
                    win = 1
                return


def remove_field(r, c):
    global fields_count
    for i in range(c + 1):
        fields[r].pop(0)
        fields_count -= 1


def generate():
    rect_height = (HEIGHT - rows * 10) / rows
    rect_width = (WIDTH - columns * 10) / columns
    for r in range(rows):
        fields.append([])
        for c in range(columns):
            rect = Rect((rect_width + 10) * c, (rect_height + 10) * r, rect_width, rect_height)
            fields[r].append(rect)


generate()
pgzrun.go()
