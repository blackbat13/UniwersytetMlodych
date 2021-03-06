import pgzrun

WIDTH = 800
HEIGHT = 800

glowa = Actor("glowa.png")
glowa.x = WIDTH / 2
glowa.y = HEIGHT / 2
glowa.vx = 0
glowa.vy = 0
glowa.czas = 0
glowa.martwy = True

waz = []
waz.append(glowa)

elementy = []

def draw():
    screen.fill((255, 255, 255))

    if glowa.martwy:
        screen.draw.text("Koniec Gry", center=(WIDTH/2, HEIGHT/2), owidth=0.5, fontsize=50, color="red")
        return

    for el in waz:
        el.draw()

    glowa.draw()



def update():
    glowa.czas += 1
    if glowa.czas == 30:
        glowa.czas = 0
    else:
        return

    for i in range(len(waz) - 1, 0, -1):
        el = waz[i]
        if el.czekaj:
            el.czekaj = False
        else:
            el.x = waz[i - 1].x
            el.y = waz[i - 1].y

    glowa.x += glowa.vx
    glowa.y += glowa.vy

    if glowa.x > WIDTH + 32:
        glowa.x = -32

    if glowa.x < -32:
        glowa.x = WIDTH + 32

    if glowa.y < -32:
        glowa.y = HEIGHT + 32

    if glowa.y > HEIGHT + 32:
        glowa.y = -32

    for i in range(1, len(waz)):
        if glowa.colliderect(waz[i]):
            glowa.martwy = True


def on_key_down(key):
    if key == keys.LEFT:
        glowa.vx = -64
        glowa.vy = 0
    if key == keys.RIGHT:
        glowa.vx = 64
        glowa.vy = 0
    if key == keys.UP:
        glowa.vx = 0
        glowa.vy = -64
    if key == keys.DOWN:
        glowa.vx = 0
        glowa.vy = 64
    if key == keys.SPACE:
        dodaj_cialo()


def dodaj_cialo():
    cialo = Actor("cialo.png")
    cialo.x = waz[-1].x
    cialo.y = waz[-1].y
    cialo.czekaj = True
    waz.append(cialo)


pgzrun.go()
