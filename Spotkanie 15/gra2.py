import pgzrun
import random

WIDTH = 800
HEIGHT = 800

kolory = ["#A3DDCB", "#E8E9A1", "#E6B566", "#E5707E"]

pilka = {"x": WIDTH / 2, "y": HEIGHT - 30, "promien": 10, "vy": 0, "kolor": random.choice(kolory)}

linie = []


def draw():
    screen.fill((0, 0, 0))

    pilka_rect = Rect((pilka["x"], pilka["y"]), (pilka["promien"] * 2, pilka["promien"] * 2))

    for linia in linie:
        for i in range(len(linia["segmenty"])):
            kolor = linia["segmenty"][i]
            szer = WIDTH / 4
            x = i * szer - linia["przes"]
            y = linia["y"]
            segment = Rect((x, y), (szer, 20))
            screen.draw.filled_rect(segment, kolor)

            if segment.colliderect(pilka_rect) and kolor != pilka["kolor"]:
                reset()

    screen.draw.filled_circle((pilka["x"], pilka["y"]), pilka["promien"], pilka["kolor"])


def dodaj_linie(y):
    linia = {}
    linia["segmenty"] = kolory[:]
    random.shuffle(linia["segmenty"])
    linia["segmenty"].extend(linia["segmenty"])
    linia["przes"] = 0
    linia["vx"] = random.randint(2, 5)
    linia["y"] = y
    linie.append(linia)


def update():
    global przes
    for linia in linie:
        linia["przes"] += linia["vx"]
        if linia["przes"] >= WIDTH:
            linia["przes"] = 0

    pilka["vy"] += 0.5
    pilka["y"] += pilka["vy"]


def on_key_down(key):
    global linia_y
    if key == keys.SPACE:
        pilka["vy"] = -10
        przesun()


def przesun():
    for linia in linie[:]:
        linia["y"] += 20
        if linia["y"] > HEIGHT:
            dodaj_linie(0)
            linie.remove(linia)


def reset():
    global pilka
    linie.clear()
    dodaj_linie(WIDTH / 2)
    dodaj_linie(WIDTH / 5)
    dodaj_linie(-80)
    pilka = {"x": WIDTH / 2, "y": HEIGHT - 30, "promien": 15, "vy": 0, "kolor": random.choice(kolory)}


reset()
pgzrun.go()
