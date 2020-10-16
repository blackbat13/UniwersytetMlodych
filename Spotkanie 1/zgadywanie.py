import random


ukryta = random.randint(1, 10)

liczba = int(input("Podaj liczbę: "))

while liczba != ukryta:
    print("Nie")

    liczba = int(input("Podaj liczbę: "))

print("Tak!")