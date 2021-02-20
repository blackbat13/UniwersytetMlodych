import pgzrun
import gamemaps
from random import randint
from datetime import datetime

WIDTH = 600
HEIGHT = 660

gracz = Actor("pacman_o")  # Load in the player Actor image
gracz.punkty = 0
gracz.zycia = 3
level = 0
PREDKOSC = 3

duchy = []
punkty = []
ruch_duchow_flaga = 4


def draw():
    screen.blit('header', (0, 0))
    screen.blit('colourmap', (0, 80))
    pacDotsLeft = 0
    for a in range(len(punkty)):
        if punkty[a].status == 0:
            punkty[a].draw()
            pacDotsLeft += 1
        if punkty[a].collidepoint((gracz.x, gracz.y)):
            if punkty[a].status == 0:
                if punkty[a].type == 2:
                    for g in range(len(duchy)): duchy[g].status = 1200
                else:
                    gracz.punkty += 10
            punkty[a].status = 1
    if pacDotsLeft == 0:
        gracz.status = 2
    rysuj_duchy()
    pobierz_grafike_gracza()
    gracz.draw()
    rysuj_zycia()
    screen.draw.text("LEVEL " + str(level), topleft=(10, 10), owidth=0.5, ocolor=(0, 0, 255), color=(255, 255, 0),
                     fontsize=40)
    screen.draw.text(str(gracz.punkty), topright=(590, 20), owidth=0.5, ocolor=(255, 255, 255), color=(0, 64, 255),
                     fontsize=60)
    if gracz.status == 3:
        drawCentreText("GAME OVER")
    if gracz.status == 2:
        drawCentreText("LEVEL CLEARED!\nPress Enter\nto Continue")
    if gracz.status == 1:
        drawCentreText("CAUGHT!\nPress Enter\nto Continue")


def drawCentreText(t):
    screen.draw.text(t, center=(300, 434), owidth=0.5, ocolor=(255, 255, 255), color=(255, 64, 0), fontsize=60)


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
    global ruch_duchow_flaga
    if gracz.status == 0:
        if ruch_duchow_flaga == 4:
            moveGhosts()
        for g in range(len(duchy)):
            if duchy[g].status > 0: duchy[g].status -= 1
            if duchy[g].collidepoint((gracz.x, gracz.y)):
                if duchy[g].status > 0:
                    gracz.punkty += 100
                    animate(duchy[g], pos=(290, 370), duration=1 / PREDKOSC, tween='linear', on_finished=zwieksz_flage)
                else:
                    gracz.zycia -= 1
                    sounds.pac2.play()
                    if gracz.zycia == 0:
                        gracz.status = 3
                        music.fadeout(3)
                    else:
                        gracz.status = 1

        if gracz.sterowanie_aktywne:
            sterowanie()
            gamemaps.sprawdz_ruch(gracz)
            if gracz.ruch_x or gracz.ruch_y:
                blokuj_sterowanie()
                sounds.pac1.play()
                animate(gracz, pos=(gracz.x + gracz.ruch_x, gracz.y + gracz.ruch_y), duration=1 / PREDKOSC,
                        tween='linear', on_finished=odblokuj_sterowanie)


def on_key_down(key):
    if key == keys.RETURN:
        if gracz.status == 1:
            gracz.status = 0
            gracz.x = 290
            gracz.y = 570
        if gracz.status == 2:
            inizjalizuj()


def inizjalizuj():
    global level
    ustaw_punkty()
    ustaw_duchy()
    gracz.x = 290
    gracz.y = 570
    gracz.status = 0
    odblokuj_sterowanie()
    level += 1
    # music.play("pm1")
    # music.set_volume(0.2)


def rysuj_zycia():
    for l in range(gracz.zycia):
        screen.blit("pacman_o", (10 + (l * 32), 40))


def pobierz_grafike_gracza():
    dt = datetime.now()
    kat = gracz.angle
    tc = dt.microsecond % (500000 / PREDKOSC) / (100000 / PREDKOSC)
    if tc > 2.5 and (gracz.ruch_x != 0 or gracz.ruch_y != 0):
        if kat != 180:
            gracz.image = "pacman_c"
        else:
            gracz.image = "pacman_cr"
    else:
        if kat != 180:
            gracz.image = "pacman_o"
        else:
            gracz.image = "pacman_or"
    gracz.angle = kat


def rysuj_duchy():
    for g in range(len(duchy)):
        if duchy[g].x > gracz.x:
            if duchy[g].status > 200 or (duchy[g].status > 1 and duchy[g].status % 2 == 0):
                duchy[g].image = "ghost5"
            else:
                duchy[g].image = "ghost" + str(g + 1) + "r"
        else:
            if duchy[g].status > 200 or (duchy[g].status > 1 and duchy[g].status % 2 == 0):
                duchy[g].image = "ghost5"
            else:
                duchy[g].image = "ghost" + str(g + 1)
        duchy[g].draw()


def moveGhosts():
    global ruch_duchow_flaga
    dmoves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ruch_duchow_flaga = 0
    for g in range(len(duchy)):
        dirs = gamemaps.dozwolone_ruchy(duchy[g])
        if w_srodku(duchy[g]):
            duchy[g].dir = 3
        else:
            if g == 0:
                sledz_gracza(g, dirs)
            if g == 1:
                zaskocz_gracza(g, dirs)

        if dirs[duchy[g].dir] == 0 or randint(0, 50) == 0:
            d = -1
            while d == -1:
                rd = randint(0, 3)
                if nad_srodkiem(duchy[g]) and rd == 1:
                    rd = 0
                if dirs[rd] == 1:
                    d = rd
            duchy[g].dir = d
        animate(duchy[g],
                pos=(duchy[g].x + dmoves[duchy[g].dir][0] * 20, duchy[g].y + dmoves[duchy[g].dir][1] * 20),
                duration=1 / PREDKOSC, tween='linear', on_finished=zwieksz_flage)


def sledz_gracza(g, dirs):
    d = duchy[g].dir
    if d == 1 or d == 3:
        if gracz.x > duchy[g].x and dirs[0] == 1:
            duchy[g].dir = 0
        if gracz.x < duchy[g].x and dirs[2] == 1:
            duchy[g].dir = 2
    if d == 0 or d == 2:
        if gracz.y > duchy[g].y and dirs[1] == 1 and not nad_srodkiem(duchy[g]):
            duchy[g].dir = 1
        if gracz.y < duchy[g].y and dirs[3] == 1:
            duchy[g].dir = 3


def zaskocz_gracza(g, dirs):
    if gracz.ruch_x > 0 and dirs[0] == 1:
        duchy[g].dir = 0
    if gracz.ruch_x < 0 and dirs[2] == 1:
        duchy[g].dir = 2

    if gracz.ruch_y > 0 and dirs[1] == 1 and not nad_srodkiem(duchy[g]):
        duchy[g].dir = 1
    if gracz.ruch_y < 0 and dirs[3] == 1:
        duchy[g].dir = 3


def w_srodku(ga):
    if ga.x > 220 and ga.x < 380 and ga.y > 320 and ga.y < 420:
        return True
    return False


def nad_srodkiem(ga):
    if ga.x > 220 and ga.x < 380 and ga.y > 300 and ga.y < 320:
        return True
    return False


def zwieksz_flage():
    global ruch_duchow_flaga
    ruch_duchow_flaga += 1


def kolizja_duchow(ga, gn):
    for g in range(len(duchy)):
        if duchy[g].colliderect(ga) and g != gn:
            return True
    return False


def ustaw_punkty():
    global punkty
    punkty = []
    a = 0
    x = 0
    while x < 30:
        y = 0
        while y < 29:
            d = gamemaps.sprawdz_punkt(10 + x * 20, 10 + y * 20)
            if d == 1:
                punkty.append(Actor("dot", (10 + x * 20, 90 + y * 20)))
                punkty[a].status = 0
                punkty[a].type = 1
                a += 1
            if d == 2:
                punkty.append(Actor("power", (10 + x * 20, 90 + y * 20)))
                punkty[a].status = 0
                punkty[a].type = 2
                a += 1
            y += 1
        x += 1


def ustaw_duchy():
    global duchy, ruch_duchow_flaga
    ruch_duchow_flaga = 4
    duchy = []
    g = 0
    while g < 4:
        duchy.append(Actor("ghost" + str(g + 1), (270 + (g * 20), 370)))
        duchy[g].dir = randint(0, 3)
        duchy[g].status = 0
        g += 1


def blokuj_sterowanie():
    gracz.sterowanie_aktywne = False


def odblokuj_sterowanie():
    gracz.ruch_x = 0
    gracz.ruch_y = 0
    gracz.sterowanie_aktywne = True


inizjalizuj()
pgzrun.go()
