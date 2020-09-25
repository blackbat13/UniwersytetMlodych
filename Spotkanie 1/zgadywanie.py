import random


ukryta = random.randint(1, 100)

liczba = int(input("Podaj liczbę: "))

while liczba != ukryta:
    if ukryta < liczba:
        print("Mniejsza!")
    if ukryta > liczba:
        print("Większa!")

    liczba = int(input("Podaj liczbę: "))

print("Trafiona!")