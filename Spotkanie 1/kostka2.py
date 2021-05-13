# Importujemy bibliotekę, która pozwoli nam generować losowe liczby
import random

# Wczytujemy od użytkownika liczbę rzutów kością, które mamy zasymulować
ile_razy = int(input("Podaj ilość rzutów kostką: "))

# W pętli od 0 do liczby rzutów minus 1
for i in range(ile_razy):
    # Symulujemy rzut kością losując liczbę całkowitą z przedziału od 1 do 6
    wynik = random.randint(1, 6)

    print("Kości zostały rzucone...")
    # Wypisujemy wylosowaną wartość na ekranie
    print("Wynik to", wynik)
