import pgzrun
import math
import random

WIDTH = 800
HEIGHT = 600

czolg = Actor("czolg.png")
czolg.x = WIDTH / 2
czolg.y = HEIGHT / 2
czolg.poziom = 1
czolg.poc_v = 3
czolg.odl_x = WIDTH
czolg.odl_y = HEIGHT
czolg.wrog_kat = 90
czolg.zycie = 1
czolg.punkty = 0

lufa = Actor("lufa.png", anchor=("middle", "bottom"))
lufa.x = WIDTH / 2
lufa.y = HEIGHT / 2
lufa.v = 3

medal = Actor("medal1.png")
medal.x = 50
medal.y = 50

pociski = []

wrogowie = []

rakiety_male = []

rakiety_duze = []

wybuchy = []

slady = []


def draw():
    screen.fill((255, 255, 255))

    for x in range(0, WIDTH + 128, 128):
        for y in range(0, HEIGHT + 128, 128):
            ziemia = Actor("ziemia1.png")
            ziemia.x = x
            ziemia.y = y
            ziemia.draw()

    for slad in slady:
        slad.draw()

    for wyb in wybuchy:
        wyb.draw()

    for wrog in wrogowie:
        wrog.draw()

    for p in pociski:
        p.draw()

    for r in rakiety_male:
        r.draw()

    for r in rakiety_duze:
        r.draw()

    czolg.draw()

    if czolg.zycie == 1:
        lufa.draw()

    if czolg.zycie == 0:
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2 - 200), fontsize=100, color="red")

    if czolg.punkty >= 10:
        if czolg.punkty >= 30:
            medal.image = "medal3"
        elif czolg.punkty >= 20:
            medal.image = "medal2"

        medal.draw()


def update():
    if keyboard.LEFT and not keyboard.SPACE:
        lufa.angle += lufa.v
    if keyboard.RIGHT and not keyboard.SPACE:
        lufa.angle -= lufa.v

    akt_pociski()
    akt_wrogowie()
    akt_rakiety_male()
    akt_rakiety_duze()
    akt_wybuchy()
    akt_slady()


def akt_slady():
    for slad in slady[:]:
        slad.czas -= 1
        if slad.czas <= 0:
            slady.remove(slad)


def akt_wybuchy():
    for wyb in wybuchy[:]:
        wyb.czas -= 1
        if wyb.czas <= 0:
            wybuchy.remove(wyb)


def akt_rakiety_duze():
    for rak in rakiety_duze:
        rak.x += math.sin(math.radians(rak.angle - 180)) * rak.v
        rak.y += math.cos(math.radians(rak.angle - 180)) * rak.v

    for rak in rakiety_duze:
        for wrog in wrogowie:
            if rak.collidepoint(wrog.pos):
                for wrog2 in wrogowie[:]:
                    odl = math.sqrt((wrog2.x - rak.x) ** 2 + (wrog2.y - rak.y) ** 2)
                    if odl <= rak.promien:
                        wybuch = Actor("wybuch3.png")
                        wybuch.x = wrog2.x
                        wybuch.y = wrog2.y
                        wybuch.angle = wrog2.angle
                        wybuch.czas = 10
                        wybuchy.append(wybuch)
                        wrogowie.remove(wrog2)
                        czolg.punkty += 2
                rakiety_duze.remove(rak)
                break


def akt_rakiety_male():
    for rak in rakiety_male:
        min_odl = 1000000000000
        min_wrog = None

        for wrog in wrogowie:
            odl = (wrog.x - rak.x) ** 2 + (wrog.y - rak.y) ** 2
            if odl < min_odl:
                min_odl = odl
                min_wrog = wrog

        if min_wrog != None:
            rak.angle = rak.angle_to(min_wrog) - 90
        rak.x += math.sin(math.radians(rak.angle - 180)) * rak.v
        rak.y += math.cos(math.radians(rak.angle - 180)) * rak.v

    for rak in rakiety_male:
        for wrog in wrogowie:
            if rak.collidepoint(wrog.pos):
                wybuch = Actor("wybuch3.png")
                wybuch.x = wrog.x
                wybuch.y = wrog.y
                wybuch.angle = wrog.angle
                wybuch.czas = 10
                wybuchy.append(wybuch)
                wrogowie.remove(wrog)
                rakiety_male.remove(rak)
                czolg.punkty += 2
                break


def akt_pociski():
    for poc in pociski:
        poc.x += math.sin(math.radians(poc.angle - 180)) * poc.v
        poc.y += math.cos(math.radians(poc.angle - 180)) * poc.v

    for poc in pociski:
        for wrog in wrogowie:
            if poc.colliderect(wrog):
                wybuch = Actor("wybuch3.png")
                wybuch.x = wrog.x
                wybuch.y = wrog.y
                wybuch.angle = wrog.angle
                wybuch.czas = 10
                wybuchy.append(wybuch)
                wrogowie.remove(wrog)
                pociski.remove(poc)
                czolg.punkty += 2
                break


def akt_wrogowie():
    if random.randint(0, 200) < czolg.poziom:
        wrog = Actor("wrog1.png")
        kat = random.randint(0, 360)
        wrog.x = WIDTH / 2 + math.sin(math.radians(kat)) * czolg.odl_x
        wrog.y = HEIGHT / 2 + math.cos(math.radians(kat)) * czolg.odl_y
        wrog.v = 2
        wrog.slad = 0
        wrogowie.append(wrog)

    for wrog in wrogowie:
        wrog.angle = wrog.angle_to(czolg) + czolg.wrog_kat
        wrog.x += math.sin(math.radians(wrog.angle)) * wrog.v
        wrog.y += math.cos(math.radians(wrog.angle)) * wrog.v
        wrog.slad -= 1
        if wrog.slad <= 0:
            wrog.slad = 20
            slad = Actor("slady1.png")
            slad.x = wrog.x
            slad.y = wrog.y
            slad.angle = wrog.angle
            slad.czas = 100
            slady.append(slad)
        if wrog.colliderect(czolg):
            czolg.zycie = 0
            czolg.image = "wybuch1.png"


def on_key_down(key):
    if key == keys.SPACE and czolg.zycie == 1:
        poc = Actor("pocisk.png")
        poc.angle = lufa.angle
        poc.x = lufa.x
        poc.y = lufa.y
        poc.v = czolg.poc_v
        pociski.append(poc)

    if key == keys.Z and czolg.zycie == 1:
        rak = Actor("rakieta1.png")
        rak.angle = lufa.angle
        rak.x = lufa.x
        rak.y = lufa.y
        rak.v = czolg.poc_v
        rakiety_male.append(rak)

    if key == keys.X and czolg.zycie == 1:
        rak = Actor("rakieta2.png")
        rak.angle = lufa.angle
        rak.x = lufa.x
        rak.y = lufa.y
        rak.v = czolg.poc_v
        rak.promien = 300
        rakiety_duze.append(rak)


def nastepny_poziom():
    czolg.poc_v += 0.25
    czolg.poziom += 1
    if czolg.poziom >= 5:
        czolg.odl_x = WIDTH / 2 - czolg.poziom * 2
        czolg.odl_y = HEIGHT / 2 - czolg.poziom * 2
        czolg.wrog_kat = 170


clock.schedule_interval(nastepny_poziom, 1)
pgzrun.go()
