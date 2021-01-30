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


def draw():
    screen.fill((255, 255, 255))

    for wrog in wrogowie:
        wrog.draw()

    for p in pociski:
        p.draw()

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

    for poc in pociski:
        poc.x += math.sin(math.radians(poc.angle - 180)) * poc.v
        poc.y += math.cos(math.radians(poc.angle - 180)) * poc.v

    if random.randint(0, 200) < czolg.poziom:
        wrog = Actor("wrog1.png")
        kat = random.randint(0, 360)
        wrog.x = WIDTH / 2 + math.sin(math.radians(kat)) * czolg.odl_x
        wrog.y = HEIGHT / 2 + math.cos(math.radians(kat)) * czolg.odl_y
        wrog.v = 2
        wrogowie.append(wrog)

    for wrog in wrogowie:
        wrog.angle = wrog.angle_to(czolg) + czolg.wrog_kat
        wrog.x += math.sin(math.radians(wrog.angle)) * wrog.v
        wrog.y += math.cos(math.radians(wrog.angle)) * wrog.v
        if wrog.colliderect(czolg):
            czolg.zycie = 0
            czolg.image = "wybuch1.png"

    for poc in pociski:
        for wrog in wrogowie:
            if poc.colliderect(wrog):
                wrogowie.remove(wrog)
                pociski.remove(poc)
                czolg.punkty += 2
                break


def on_key_down(key):
    if key == keys.SPACE and czolg.zycie == 1:
        poc = Actor("pocisk.png")
        poc.angle = lufa.angle
        poc.x = lufa.x
        poc.y = lufa.y
        poc.v = czolg.poc_v
        pociski.append(poc)


def nastepny_poziom():
    czolg.poc_v += 0.25
    czolg.poziom += 1
    if czolg.poziom >= 5:
        czolg.odl_x = WIDTH / 2 - czolg.poziom * 2
        czolg.odl_y = HEIGHT / 2 - czolg.poziom * 2
        czolg.wrog_kat = 170


clock.schedule_interval(nastepny_poziom, 8)
pgzrun.go()
