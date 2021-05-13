# Importujemy bibliotekę, która pozwoli nam generować losowe liczby
import random

# Losujemy liczbę całkowitą z przedziału od 1 do 10
ukryta = random.randint(1, 10)

# Wczytujemy liczbę od użytkownika
liczba = int(input("Podaj liczbę: "))

# Dopóki użytkownik nie odgadł, jaką liczbę wylosował komputer
while liczba != ukryta:
    # Wypisujemy stosowny komunikat na ekranie
    print("Nie")

    # Ponownie prosimy użytkownika o podanie liczby
    liczba = int(input("Podaj liczbę: "))

# Skoro wyszliśmy z pętli, to znaczy, że użytkownik odgadł wyosowaną przez komputer liczbę
# Wypisujemy więc stosowny komunikat
print("Tak!")
