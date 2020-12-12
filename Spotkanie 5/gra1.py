import pgzrun
import random
import pygame

WIDTH = 600
HEIGHT = 900

statek = Actor("statek")
statek.x = WIDTH / 2
statek.y = HEIGHT - 60
statek.px = 5

meteory = []


def draw():
    screen.blit("tlo", (0, 0))
    statek.draw()

    for met in meteory:
        met.draw()


def update():
    mysz_x, mysz_y = pygame.mouse.get_pos()
    if mysz_x < statek.x:
        statek.x -= statek.px
    if mysz_x > statek.x:
        statek.x += statek.px

    if random.randint(0, 250) <= 1:
        dodaj_meteor()

    for met in meteory:
        met.y += met.py
        if met.y > HEIGHT + 50:
            meteory.remove(met)


def dodaj_meteor():
    grafika = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    met = Actor(grafika)
    met.x = random.randint(20, WIDTH - 20)
    met.y = -10
    met.py = random.randint(2, 10)
    meteory.append(met)


pgzrun.go()
