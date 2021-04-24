import socket

server = "127.0.0.1"  # Adres IP serwera
port = 5555
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

user_name = input("Podaj swój nick: ")
print("Wyszukiwanie rozmówcy...")
connection.connect((server, port))  # Lączymy się z serwerem
connection.send(str.encode(user_name))
user2_name = connection.recv(2048).decode()
order = int(connection.recv(2048).decode())
print("Połączono z użytkownikiem", user2_name)
if order == 0:
    print("Przywitaj się!")
else:
    print("Poczekaj na wiadomość")

while True:
    if order == 0:
        message = input("Wiadomość: ")
        connection.send(str.encode(message))
        order = 1
    else:
        message = connection.recv(2048).decode()
        print(user2_name, ":", message)
        order = 0
