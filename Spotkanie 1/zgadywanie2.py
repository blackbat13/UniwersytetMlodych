# Importujemy bibliotekę, która pozwoli nam generować losowe liczby
import random

# Losujemy liczbę całkowitą z przedziału od 1 do 100
ukryta = random.randint(1, 100)

# Wczytujemy liczbę od użytkownika
liczba = int(input("Podaj liczbę: "))

# Dopóki użytkownik nie odgadł, jaką liczbę wylosował komputer
while liczba != ukryta:
    # Jeżeli wylosowana wartość jest mniejsza od tej podanej przez użytkownika
    if ukryta < liczba:
        # Informujemy użytkownika o tym, że wartość, której szuka, jest mniejsza
        print("Mniejsza!")

    # Jeżeli wylosowana wartość jest większa od tej podanej przez użytkownika
    if ukryta > liczba:
        # Informaujemy użytkownika o tym, że wartość, której szuka, jest większa
        print("Większa!")

    # Ponownie prosimy użytkownika o podanie liczby
    liczba = int(input("Podaj liczbę: "))

# Skoro wyszliśmy z pętli, to znaczy, że użytkownik odgadł wyosowaną przez komputer liczbę
# Wypisujemy więc stosowny komunikat
print("Trafiona!")