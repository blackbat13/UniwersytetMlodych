import socket
from _thread import *
import random

server = "192.168.1.39"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server, port))  # Lączymy gniazdo ze wskazanym adresem IP i portem
s.listen(2)  # Nasłuchujemy na połączenia


def threaded_client(user1, user2):  # Obsługa graczy i ich gry
    user1.send(str.encode("1"))
    user2.send(str.encode("2"))

    rows = random.randint(2, 5)
    columns = random.randint(3, 8)

    configuration = str((rows, columns))
    user1.send(str.encode(configuration))
    user2.send(str.encode(configuration))

    nick1 = user1.recv(2048).decode()
    nick2 = user2.recv(2048).decode()
    user1.send(str.encode(nick2))
    user2.send(str.encode(nick1))

    while True:  # Przez cały czas
        move = user1.recv(2048).decode()
        # print(move)
        user2.send(str.encode(move))

        move = user2.recv(2048).decode()
        # print(move)
        user1.send(str.encode(move))


print("Starting server...")
while True:  # Serwer działa cały czas
    # Czekamy na połączenie od pierwszego rozmówcy
    user1, addr1 = s.accept()
    print("Connected to:", addr1)

    # Czekamy na połączenie od drugiego rozmówcy
    user2, addr2 = s.accept()
    print("Connected to:", addr2)

    # Uruchamiamy wątek do obsługi komunikacji pomiędzy graczami
    start_new_thread(threaded_client, (user1, user2))
