import random


ile_razy = int(input("Podaj ilość rzutów kostką: "))

for i in range(ile_razy):
    wynik = random.randint(1, 6)

    print("Kości zostały rzucone...")
    print("Wynik to", wynik)