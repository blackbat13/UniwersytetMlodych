import socket

# Podajemy adres IP serwera
server = "127.0.0.1"
# A także port, na którym serwer nasłuchuje
port = 5555

# Tworzymy gniazdo do połączeń
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wczytujemy nick użytkownika
user_name = input("Podaj swój nick: ")
print("Wyszukiwanie rozmówcy...")

# Ustanawiamy połączenie z serwerem
connection.connect((server, port))

# Wysyłamy nasz nick do serwera
connection.send(str.encode(user_name))

# Odbieramy nick drugiego rozmówcy od serwera
user2_name = connection.recv(2048).decode()

# Odbieramy numer naszej kolejności od serwera
order = int(connection.recv(2048).decode())

print("Połączono z użytkownikiem", user2_name)

if order == 1:
    print("Przywitaj się!")
else:
    print("Poczekaj na wiadomość")

# W nieskończonej pętli
while True:
    # Sprawdzamy, czy jest nasza kolej
    if order == 1:
        # Jeżeli jest nasza kolej, to wczytujemy wiadomość od użytkownika
        message = input("Wiadomość: ")
        # A następnie wysyłamy wiadomość do serwera
        connection.send(str.encode(message))
        # I teraz jest kolej naszego rozmówcy
        order = 2
    else:
        # Jeżeli to nasz rozmówca ma teraz swoją kolej
        # To odbieramy wiadomość od serwera
        message = connection.recv(2048).decode()
        # Wyświetlamy ją na ekranie
        print(user2_name, ":", message)
        # I przechodzimy do naszej "tury"
        order = 1
