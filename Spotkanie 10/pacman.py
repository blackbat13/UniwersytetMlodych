import pgzrun
import gamemaps
import datetime

WIDTH = 600
HEIGHT = 660

gracz = Actor("pacman_o")
PREDKOSC = 3

punkty = []  # Tworzymy listę punktów


def inicjalizuj():
    gracz.x = 290
    gracz.y = 570
    gracz.status = 0
    # music.play("pm1")
    # music.set_volume(0.2)
    ustawPunkty()
    odblokuj_sterowanie()
    gracz.lastKeyPressed = ""


def ustawPunkty():
    punkt_indeks = 0
    for x in range(30):
        for y in range(29):
            if gamemaps.sprawdz_punkt(10 + x * 20, 10 + y * 20):  # Sprawdzamy, czy możemy postawić punkt
                punkty.append(Actor("dot", (10 + x * 20, 90 + y * 20)))  # Dodajemy nowy punkt
                punkty[punkt_indeks].status = 0  # Ustawiamy jego status na niezebrany
                punkt_indeks += 1


def draw():
    screen.blit('header', (0, 0))
    screen.blit('colourmap', (0, 80))
    for i in range(len(punkty)):  # Przechodzimy przez wszystkie punkty
        if punkty[i].status == 0:  # Jeżeli punkt nie został zjedzony
            punkty[i].draw()  # Narysuj punkt
        if punkty[i].collidepoint((gracz.x, gracz.y)):
            punkty[i].status = 1

    pobierz_grafike_gracza()  # Ustalamy odpowiednią grafikę dla gracza
    gracz.draw()  # Rysujemy gracza


def blokuj_sterowanie():
    global gracz
    gracz.sterowanie_aktywne = False


def odblokuj_sterowanie():
    global gracz
    gracz.sterowanie_aktywne = True
    gracz.ruch_x = 0
    gracz.ruch_y = 0


def sterowanie():
    if keyboard.left:
        gracz.angle = 180
        gracz.ruch_x = -20
    if keyboard.right:
        gracz.angle = 0
        gracz.ruch_x = 20
    if keyboard.up:
        gracz.angle = 90
        gracz.ruch_y = -20
    if keyboard.down:
        gracz.angle = 270
        gracz.ruch_y = 20


def update():
    global gracz
    if gracz.status == 0:  # gracz żyje
        if gracz.sterowanie_aktywne:  # jeżeli wejście jest aktywne
            sterowanie()  # sprawdzamy wejście z klawiatury
            gamemaps.sprawdz_ruch(gracz)  # sprawdzamy, czy możemy poruszyć graczem
            if gracz.ruch_x or gracz.ruch_y:
                sounds.pac1.play()
                blokuj_sterowanie()
                animate(gracz, pos=(gracz.x + gracz.ruch_x, gracz.y + gracz.ruch_y), duration=1 / PREDKOSC,
                        tween='linear', on_finished=odblokuj_sterowanie)
                # wykonaj animację ruchu gracza
                # po zakończeniu animacji odblokuj wejście


def pobierz_grafike_gracza():  # Pobranie właściwej grafiki
    dt = datetime.datetime.now()
    kat = gracz.angle
    tc = dt.microsecond % (500000 / PREDKOSC) / (100000 / PREDKOSC)  # ustalenie czasu
    if tc > 2.5 and (gracz.ruch_x != 0 or gracz.ruch_y != 0):  # jeżeli jesteśmy w trakcie ruchu
        if kat != 180:
            gracz.image = "pacman_c"
        else:
            gracz.image = "pacman_cr"
    else:  # grafika w trakcie postoju
        if kat != 180:
            gracz.image = "pacman_o"
        else:
            gracz.image = "pacman_or"
    gracz.angle = kat


inicjalizuj()
pgzrun.go()
