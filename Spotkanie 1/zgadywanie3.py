import random

ukryta = random.randint(1, 100)

ile_prob = 1
liczba = int(input("Podaj liczbę: "))

while liczba != ukryta:
    if ukryta < liczba:
        print("Mniejsza!")
    if ukryta > liczba:
        print("Większa!")

    ile_prob += 1
    liczba = int(input("Podaj liczbę: "))

print("Trafiona!")
print("Liczba prób:", ile_prob)
