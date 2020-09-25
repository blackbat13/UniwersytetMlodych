import random

ile_razy = int(input("Podaj ilość rzutów kostką: "))

szostki = 0

for i in range(ile_razy):
    wynik = random.randint(1, 6)

    print("Kości zostały rzucone...")
    print("Wynik to", wynik)

    if wynik == 6:
        szostki += 1

print("Szóstka wypadła", szostki, "razy")
