import pgzrun
import random

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 700

# Ustawiamy siłę grawitacji - im większa, tym ptak będzie szybciej spadał
grawitacja = 0.3

# Tworzymy naszą postać - ptaka
ptak = Actor("ptak1", (75, 200))
ptak.py = 0  # Nadajemy mu początkową prędkość - 0
ptak.martwy = True  # Na początku ptak jest martwy
ptak.wynik = 0  # Wynik gracza na początku gry to 0
ptak.y = HEIGHT + 20  # Ustawiamy ptaka pod ekranem

# Tworzymy dwie rury - górną i dolną
# Nadajemy im odpowiednie kotwice (achor), żeby łatwiej je ustawiać
rura_gora = Actor("gora", anchor=("left", "bottom"))
rura_dol = Actor("dol", anchor=("left", "top"))

# Tworzymy przycisk start
start = Actor("start1")
start.x = WIDTH / 2
start.y = HEIGHT / 2


def draw():
    # Zamiast kolorem, tło wypełniamy grafiką, której lewy górny róg będzie w lewym górnym rogu ekranu
    screen.blit("tlo", (0, 0))

    # Jeżeli ptak wypadł poza ekran, to wyświetlamy menu
    if ptak.y > HEIGHT:
        start.draw()
    else:
        # W przeciwnym przypadku wyświetlamy grę - ptaka i rury
        rura_gora.draw()
        rura_dol.draw()
        ptak.draw()

    # Wyświetlamy obecny wynik na ekranie
    screen.draw.text(str(ptak.wynik), midtop=(WIDTH // 2, 10), fontsize=70)


def update():
    # Dodajemy siłę grawitacji do prędkości spadania/lotu ptaka
    ptak.py += grawitacja
    # PRzemieszczamy ptaka zgodnie z jego prędkością
    ptak.y += ptak.py

    # Jeżeli ptak jest martwy, to nic więcej nie robimy
    if ptak.martwy:
        return

    # Przesuwamy rury w lewo
    rura_gora.left -= 3
    rura_dol.left -= 3

    # W zależności od prędkości ptaka, ustawiamy jego grafikę i kąt obrotu
    if ptak.py < 0:
        # Ptak leci do góry
        ptak.image = "ptak2"
        ptak.angle += 3
    else:
        # Ptak leci na dół
        ptak.image = "ptak1"
        ptak.angle -= 3

    # Ograniczamy maksymalny kąt obrotu ptaka do 45 stopni
    if ptak.angle > 45:
        ptak.angle = 45
    if ptak.angle < -45:
        ptak.angle = -45

    # Jeżeli rura wyszła z lewej strony ekranu
    if rura_gora.x < -100:
        # Ustawiamy rury na nowo
        ustaw_rury()
        ptak.wynik += 1
        sounds.point.play()

    # Jeżeli ptak uderzył w górną lub dolną rurę
    if ptak.colliderect(rura_gora) or ptak.colliderect(rura_dol):
        # Zmieniamy grafikę ptaka i jego obrót
        ptak.image = "martwy"
        ptak.martwy = True
        ptak.angle = -90
        sounds.hit.play()

    # Jeżeli ptak wyleciał poza ekran z góry lub z dołu
    if ptak.y > HEIGHT or ptak.y < 0:
        # Zmieniamy grafikę ptaka i jego obrót
        ptak.image = "martwy"
        ptak.martwy = True
        ptak.angle = -90
        sounds.die.play()


# Gdy poruszamy myszą
def on_mouse_move(pos):
    # Sprawdzamy, czy przycisk myszy znajduje się na przycisku, czy poza nim
    # I ustawiamy odpowiednią grafikę
    if start.collidepoint(pos):
        start.image = "start2"
    else:
        start.image = "start1"


# Gdy klikniemy myszką
def on_mouse_down(pos):
    # Jeżeli kliknęliśmy na przycisk, to startujemy grę
    if start.collidepoint(pos):
        resetuj()


# Gdy klikniemy dowolny klawisz na klawiaturze, to ptak zwiększa swoją prędkość latania, jeżeli jeszcze żyje
def on_key_down():
    if not ptak.martwy:
        ptak.py = -7
        sounds.wing.play()


# Resetujemy grę
def resetuj():
    ptak.y = 200
    ptak.martwy = False
    ptak.wynik = 0
    ptak.py = 0
    ptak.image = "ptak1"
    ustaw_rury()


# Ustawiamy kolejne rury
def ustaw_rury():
    # Losujemy pozycję przerwy pomiędzy rurami
    przerwa = random.randint(200, 500)
    rura_gora.pos = (WIDTH, przerwa - 70)
    rura_dol.pos = (WIDTH, przerwa + 70)


# Na samym początku ustawiamy pierwsze rury
ustaw_rury()
pgzrun.go()
