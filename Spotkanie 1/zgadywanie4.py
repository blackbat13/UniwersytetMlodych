# Importujemy bibliotekę, która pozwoli nam generować losowe liczby
import random

# Prosimy użytkownika o podanie zakresu, z którego ma być wylosowana liczba
print("Podaj zakres")

# Wczytujemy początek zakresu i zamieniamy na liczbę całkowitą
od = int(input("Od:"))

# Wczytujemy koniec zakresu i zamieniamy na liczbę całkowitą
do = int(input("Do:"))

# Jeżeli początek zakresu jest większy od jego końca
if od > do:
    # To znaczy, że zakres jest błędny, informujemy więc o tym użytkownika
    print("Błędny zakres!")
    # A następnie kończymy działanie programu
    exit()

# Losujemy liczbę całkowitą z przedziału podanego przez użytkownika
ukryta = random.randint(od, do)

# Będziemy zliczać liczbę prób, które potrzebował użytkownik, żeby odgadnąć wartość
# Zaczynamy liczyć od 1
ile_prob = 1

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

    # Zliczamy kolejną próbę zwiększając wartość licznika ile_prob
    ile_prob += 1

    # Ponownie prosimy użytkownika o podanie liczby
    liczba = int(input("Podaj liczbę: "))

# Skoro wyszliśmy z pętli, to znaczy, że użytkownik odgadł wyosowaną przez komputer liczbę
# Wypisujemy więc stosowny komunikat
print("Trafiona!")

# Wypisujemy także liczbę prób podjętych przez użytkownika
print("Liczba prób:", ile_prob)
