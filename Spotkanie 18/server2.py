import socket
import random
from _thread import *

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server, port))  # Lączymy gniazdo ze wskazanym adresem IP i portem
s.listen(2)  # Nasłuchujemy na połączenia


def threaded_client(player1, player2):  # Obsługa graczy i ich gry
    # Wysyłamy graczom ich numery
    player1.send(str.encode("0"))  # Wyślij do gracza 1 jego numer - 0
    player2.send(str.encode("1"))  # Wyślij do gracza 2 jego numer - 1
    seed = random.randint(100, 5000)
    player1.send(str.encode(str(seed)))
    player2.send(str.encode(str(seed)))

    while True:  # Przez cały czas
        # Odbieramy ruch gracza 1 i wysyłamy go do gracza 2
        move = player1.recv(2048).decode()  # Odbieramy ruch gracza i go "dekodujemy"
        player2.send(str.encode(move))  # Wysyłamy ruch do drugiego gracza

        # Odbieramy ruch gracza 2 i wysyłamy go do gracza 1
        move = player2.recv(2048).decode()
        player1.send(str.encode(move))

print("Starting server...")
while True:  # Serwer działa cały czas
    # Czekamy na połączenie od pierwszego gracza
    player1, addr1 = s.accept()
    print("Connected to:", addr1)
    # Czekamy na połączenie od drugiego gracza
    player2, addr2 = s.accept()
    print("Connected to:", addr2)

    # Uruchamiamy wątek do obsługi komunikacji pomiędzy graczami
    start_new_thread(threaded_client, (player1, player2))
