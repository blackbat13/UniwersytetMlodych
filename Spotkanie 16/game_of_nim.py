import pgzrun


WIDTH = 800
HEIGHT = 1000

rows = 2
columns = 5

fields = []


def draw():
    screen.fill("white")
    for row in fields:
        for el in row:
            screen.draw.filled_rect(el, "red")

def on_mouse_down(pos):
    for r in range(len(fields)):
        for c in range(len(fields[r])):
            if fields[r][c].collidepoint(pos):
                remove_field(r, c)
                return

def remove_field(r, c):
    for i in range(c + 1):
        fields[r].pop(0)

def generate():
    rect_height = (HEIGHT - rows*10) / rows
    rect_width = (WIDTH - columns*10) / columns
    for r in range(rows):
        fields.append([])
        for c in range(columns):
            rect = Rect((rect_width+10)*c, (rect_height+10)*r, rect_width, rect_height)
            fields[r].append(rect)


generate()
pgzrun.go()