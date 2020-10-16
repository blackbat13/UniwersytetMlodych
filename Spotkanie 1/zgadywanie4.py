import random

print("Podaj zakres")
od = int(input("Od:"))
do = int(input("Do:"))

if od > do:
    print("Błędny zakres!")
    exit()

ukryta = random.randint(od, do)

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
