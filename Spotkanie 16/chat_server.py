import socket
from _thread import *

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server, port))  # Lączymy gniazdo ze wskazanym adresem IP i portem
s.listen(2)  # Nasłuchujemy na połączenia


def threaded_client(user1, user2):  # Obsługa graczy i ich gry
    user1_name = user1.recv(2048).decode()  # Pobieramy nick pierwszego rozmówcy
    user2_name = user2.recv(2048).decode()  # Pobieramy nick drugiego rozmówcy

    user1.send(str.encode(user2_name))
    user2.send(str.encode(user1_name))

    user1.send(str.encode("0"))
    user2.send(str.encode("1"))

    while True:  # Przez cały czas
        message = user1.recv(2048).decode()
        user2.send(str.encode(message))

        message = user2.recv(2048).decode()
        user1.send(str.encode(message))

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
