import random
import socket
import time
from _thread import *

WIDTH = 800
HEIGHT = 1000
block_size = 50


def threaded_client(user1, user2):  # Obsługa graczy i ich gry
    # Pobieramy nicki od rozmówców
    user1_name = user1.recv(2048).decode()
    user2_name = user2.recv(2048).decode()

    # Następnie wysyłamy te nicki do rozmówców, zapoznając ich ze sobą
    user1.send(str.encode(user2_name))
    user2.send(str.encode(user1_name))

    # Wysyłamy rozmówcom ich kolejność
    user1.send(str.encode("1"))
    user2.send(str.encode("2"))

    hitmans_count = random.randint(2, 5)

    hitmans = [{"y": block_size / 2} for i in range(hitmans_count + 1)]

    user1.send(str.encode(str(hitmans_count)))
    user2.send(str.encode(str(hitmans_count)))

    user1.setblocking(False)
    user2.setblocking(False)

    start = time.perf_counter()

    # Obsługujemy rozmowę przez cał czas
    while True:
        stop = time.perf_counter()
        if stop - start > 0.2:
            start = stop
            type = random.randint(1, hitmans_count)
            move = random.randint(-1, 1)

            new_y = hitmans[type]["y"]
            new_y += move * block_size
            if 0 < new_y < HEIGHT:
                hitmans[type]["y"] = new_y
                message = (type, move, random.randint(5, 20))
                user1.send(str.encode(str(message)))
                user2.send(str.encode(str(message)))
            # print(message)

        try:
            # Pobieramy wiadomość od pierwszego rozmówcy
            message = user1.recv(2048).decode()
            # I wysyłamy ją do drugiego
            user2.send(str.encode(message))
        except:
            pass

        try:
            # Następnie pobieramy wiadomość od drugiego rozmówcy
            message = user2.recv(2048).decode()
            # I wysyłamy ją do pierwszego
            user1.send(str.encode(message))
        except:
            pass


# Podajemy adres IP, na którym będzie działał serwer
server = "127.0.0.1"
# A także port, na którym będzie nasłuchiwał na połączenia
port = 5555

# Tworzymy gniazdo
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lączymy gniazdo ze wskazanym adresem IP i portem
s.bind((server, port))

# Nasłuchujemy na połączenia
s.listen(2)

print("Starting server...")
# Serwer działa cały czas
while True:
    # Czekamy na połączenie od pierwszego rozmówcy
    user1, addr1 = s.accept()
    print("Connected to:", addr1)

    # Czekamy na połączenie od drugiego rozmówcy
    user2, addr2 = s.accept()
    print("Connected to:", addr2)

    # Uruchamiamy wątek do obsługi komunikacji pomiędzy użytkownikami
    start_new_thread(threaded_client, (user1, user2))
