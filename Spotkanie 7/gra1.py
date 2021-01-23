import pgzrun

WIDTH = 640
HEIGHT = 640

pole_rozmiar = 64

mapa_plik = open("mapa.txt")
mapa = [list(map(int, line.split(" "))) for line in mapa_plik.readlines()]
mapa_plik.close()

obiekty_plik = open("obiekty.txt")
obiekty = [list(map(int, line.split(" "))) for line in obiekty_plik.readlines()]
obiekty_plik.close()


mapa_grafiki = ["trawa1.png", "woda1.png", "woda2.png", "woda3.png", "woda4.png", "woda5.png", "ziemia1.png"]

obiekty_grafiki = ["", "drzewo1.png", "drzewo2.png", "drzewo3.png", "drzewo4.png", "krzak1.png", "krzak2.png"]

gracz = Actor("postac3.png", anchor=("left", "top"))
gracz.pole_x = 21
gracz.pole_y = 21

gracz.x = 5 * pole_rozmiar
gracz.y = 5 * pole_rozmiar


def draw():
    screen.fill((255, 255, 255))

    # Wypełniamy ekran polami
    for x in range(0, 10):
        for y in range(0, 10):
            mapa_obraz = mapa_grafiki[mapa[y + gracz.pole_y][x + gracz.pole_x]]

            pole = Actor(mapa_obraz, anchor=("left", "top"))
            pole.x = x * pole_rozmiar
            pole.y = y * pole_rozmiar
            pole.draw()



    gracz.draw()

    for x in range(0, 10):
        for y in range(0, 10):
            obiekt_numer = obiekty[y + gracz.pole_y][x + gracz.pole_x]
            if obiekt_numer != 0:
                obiekt_obraz = obiekty_grafiki[obiekt_numer]
                obiekt = Actor(obiekt_obraz, anchor=("left", "top"))
                obiekt.x = x * pole_rozmiar
                obiekt.y = y * pole_rozmiar
                obiekt.draw()

def on_key_down(key):
    if key == keys.RIGHT:
        gracz.pole_x += 1
    if key == keys.LEFT:
        gracz.pole_x -= 1
    if key == keys.UP:
        gracz.pole_y -= 1
    if key == keys.DOWN:
        gracz.pole_y += 1

pgzrun.go()
