from pygame import image, Color

obraz_ruchy = image.load('images/pacmanmovemap.png')
obraz_punkty = image.load('images/pacmandotmap.png')


def sprawdz_ruch(p):
    if p.x + p.ruch_x < 0:
        p.x = p.x + 600
    if p.x + p.ruch_x > 600:
        p.x = p.x - 600
    if obraz_ruchy.get_at((int(p.x + p.ruch_x), int(p.y + p.ruch_y - 80))) != Color('black'):
        p.ruch_x = 0
        p.ruch_y = 0


def sprawdz_punkt(x, y):
    if obraz_punkty.get_at((int(x), int(y))) == Color('black'):
        return True
    return False


def dozwolone_ruchy(g):
    if g.x - 20 < 0:
        g.x = g.x + 600
    if g.x + 20 > 600:
        g.x = g.x - 600
    kierunki = [0, 0, 0, 0]
    if g.x + 20 < 600:
        if obraz_ruchy.get_at((int(g.x + 20), int(g.y - 80))) == Color('black'):
            kierunki[0] = 1
    if g.x < 600 and g.x >= 0:
        if obraz_ruchy.get_at((int(g.x), int(g.y - 60))) == Color('black'):
            kierunki[1] = 1
    if g.x - 20 >= 0:
        if obraz_ruchy.get_at((int(g.x - 20), int(g.y - 80))) == Color('black'):
            kierunki[2] = 1
    if g.x < 600 and g.x >= 0:
        if obraz_ruchy.get_at((int(g.x), int(g.y - 100))) == Color('black'):
            kierunki[3] = 1
    return kierunki
