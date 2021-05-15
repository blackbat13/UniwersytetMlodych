import random
import pgzrun
import socket
import ast

WIDTH = 800
HEIGHT = 1000

# Podajemy adres IP serwera
server = "127.0.0.1"
# A także port, na którym serwer nasłuchuje
port = 5555

# Tworzymy gniazdo do połączeń
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ustanawiamy połączenie z serwerem
connection.connect((server, port))

# Podajemy nick użytkownika
user_name = "blackbat"

# Wysyłamy nasz nick do serwera
connection.send(str.encode(user_name))

# Odbieramy nick drugiego rozmówcy od serwera
opponent_name = connection.recv(2048).decode()

# Odbieramy numer naszej kolejności od serwera
order = int(connection.recv(2048).decode())

hitmans_count = int(connection.recv(2048).decode())
print(hitmans_count)

# Ustawiamy gniazdo w trybie nieblokowania, tak żaby gra się nie zawieszała podczas czekania na wiadomość od serwera
connection.setblocking(False)

block_size = 50

man = Actor("man")
man.x = WIDTH / 2
man.y = HEIGHT - block_size / 2
man.angle = 90

hitmans = []
bullets = []


def generate_hitmans():
    for i in range(hitmans_count):
        hitman = Actor("hitman")
        if i % 2 == 0:
            hitman.x = block_size / 2
        else:
            hitman.x = WIDTH - block_size / 2
            hitman.angle = 180
        hitman.y = block_size / 2
        hitman.can_shoot = True
        hitmans.append(hitman)


def draw():
    screen.fill("black")
    man.draw()
    for hit in hitmans:
        hit.draw()

    for bul in bullets:
        bul.draw()


def update():
    try:
        type, move, speed = ast.literal_eval(connection.recv(2048).decode())

        if type == -1:
            man.y += block_size * move
            if man.y < 0:
                man.y = HEIGHT - block_size / 2
        else:
            if move == 0:
                bul = Actor("bullet")
                bul.x = hitmans[type].x
                bul.y = hitmans[type].y
                if type % 2 == 0:
                    bul.angle = -90
                    bul.vx = speed
                else:
                    bul.angle = 90
                    bul.vx = -speed
                bullets.append(bul)
            else:
                hitmans[type].y += move * block_size
    except:
        pass

    for bul in bullets[:]:
        bul.x += bul.vx

        if bul.colliderect(man):
            man.y = HEIGHT - block_size / 2

        if bul.x > WIDTH:
            bullets.remove(bul)


def on_key_down(key):
    if order == 1:
        if key == keys.UP:
            man.y -= block_size
            move = (-1, -1, 0)
            connection.send(str.encode(str(move)))
            if man.y < 0:
                man.y = HEIGHT - block_size / 2
    if order == 2:
        if key == keys.UP:
            hitmans[0].y -= block_size
            move = (0, -1, 0)
            connection.send(str.encode(str(move)))
        if key == keys.DOWN:
            hitmans[0].y += block_size
            move = (0, 1, 0)
            connection.send(str.encode(str(move)))
        if key == keys.SPACE and hitmans[0].can_shoot:
            bul = Actor("bullet")
            bul.x = hitmans[0].x
            bul.y = hitmans[0].y
            bul.angle = -90
            bul.vx = random.randint(5, 20)
            bullets.append(bul)
            move = (0, 0, bul.vx)
            connection.send(str.encode(str(move)))
            hitmans[0].can_shoot = False
            clock.schedule(unlock_hitman, 0.3)


def unlock_hitman():
    hitmans[0].can_shoot = True


generate_hitmans()
pgzrun.go()
