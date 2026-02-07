"""

Roomba Visualization (Python turtle)
- Grid: 10x10 cells (0..9, 0..9)
- Dock at (0,0) top-left (we draw top-left as (0,0) in grid coords)
- Roomba does serpentine scan until it finds dirt, then returns to dock

Adjustable:
  CELL      : pixel size of one grid cell
  SPEED     : turtle speed (0 = fastest, 1..10 slower)
  STEP_DELAY: time.sleep between moves
"""

import turtle
import time
import random

# =========================
# CONFIG
# =========================
MaxX, MaxY = 9, 9          # grid coords: x in [0..9], y in [0..9]
dockX, dockY = 0, 0

# choose dirt location (fixed or random)
# dirtX, dirtY = 5, 6
dirtX, dirtY = random.choice([(x, y) for x in range(MaxX + 1) for y in range(MaxY + 1) if not (x == dockX and y == dockY)])

CELL = 50                  # pixels per grid cell
SPEED = 0                  # 0 fastest, 1..10 slower
STEP_DELAY = 0.10          # seconds per move (increase to slow down)

# Screen padding
PAD = 80

# =========================
# COORD CONVERSION
# grid (0,0)=top-left  -> turtle (px,py) with origin at screen center
# =========================
GRID_W = (MaxX + 1) * CELL
GRID_H = (MaxY + 1) * CELL

LEFT = -GRID_W / 2
TOP  =  GRID_H / 2

def grid_to_world(gx, gy):
    # gx increases to the right, gy increases downward (top-left origin)
    wx = LEFT + gx * CELL + CELL / 2
    wy = TOP  - gy * CELL - CELL / 2
    return wx, wy

# =========================
# DRAWING HELPERS
# =========================
def draw_grid(pen):
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(2)
    pen.up()

    # outer border
    pen.goto(LEFT, TOP)
    pen.down()
    pen.goto(LEFT + GRID_W, TOP)
    pen.goto(LEFT + GRID_W, TOP - GRID_H)
    pen.goto(LEFT, TOP - GRID_H)
    pen.goto(LEFT, TOP)
    pen.up()

    # inner lines
    pen.pensize(1)
    for i in range(1, MaxX + 1):
        x = LEFT + i * CELL
        pen.goto(x, TOP)
        pen.down()
        pen.goto(x, TOP - GRID_H)
        pen.up()

    for j in range(1, MaxY + 1):
        y = TOP - j * CELL
        pen.goto(LEFT, y)
        pen.down()
        pen.goto(LEFT + GRID_W, y)
        pen.up()

def stamp_cell(t, gx, gy, color, shape="square"):
    t.shape(shape)
    t.shapesize(stretch_wid=(CELL / 20) * 0.5, stretch_len=(CELL / 20) * 0.5)  # reasonable sizing
    t.color(color)
    t.up()
    t.goto(*grid_to_world(gx, gy))
    t.stamp()

def write_label(writer, gx, gy, text, color="black"):
    writer.up()
    writer.color(color)
    writer.goto(*grid_to_world(gx, gy))
    writer.goto(writer.xcor() - CELL * 0.35, writer.ycor() - 8)
    writer.write(text, font=("Arial", 10, "normal"))

# =========================
# SETUP TURTLE SCREEN
# =========================
screen = turtle.Screen()
screen.title("Roomba Turtle Visualization")
screen.setup(width=GRID_W + PAD, height=GRID_H + PAD)
screen.tracer(False)  # manual updates for smoothness

# Pen for grid
grid_pen = turtle.Turtle(visible=False)
draw_grid(grid_pen)

# Mark dock and dirt
marker = turtle.Turtle(visible=False)
marker.speed(0)

# Dock = blue
stamp_cell(marker, dockX, dockY, "dodgerblue")
# Dirt = brown
stamp_cell(marker, dirtX, dirtY, "sienna")

# Labels
writer = turtle.Turtle(visible=False)
writer.speed(0)
write_label(writer, dockX, dockY, "DOCK", "dodgerblue")
write_label(writer, dirtX, dirtY, "DIRT", "sienna")

# Roomba turtle
roomba = turtle.Turtle()
roomba.shape("circle")
roomba.color("black")
roomba.shapesize(1.0, 1.0)
roomba.speed(SPEED)
roomba.up()

# Trail turtle (optional path dots)
trail = turtle.Turtle(visible=False)
trail.speed(0)
trail.up()
trail.color("gray")

# =========================
# MOVEMENT + SIM LOGIC
# =========================
x, y = dockX, dockY

def move_to(gx, gy):
    """Move roomba to (gx,gy) and draw a small trail dot."""
    roomba.goto(*grid_to_world(gx, gy))
    trail.goto(*grid_to_world(gx, gy))
    trail.dot(6)  # path dot
    screen.update()
    time.sleep(STEP_DELAY)

def check_dirt(gx, gy):
    return gx == dirtX and gy == dirtY

# Place roomba at dock
move_to(x, y)

# Serpentine scan
dirtFound = check_dirt(x, y)

while y <= MaxY and not dirtFound:
    # even row -> move right, odd row -> move left
    if y % 2 == 0:
        x_range = range(x + 1, MaxX + 1)
    else:
        x_range = range(x - 1, -1, -1)

    for nx in x_range:
        x = nx
        move_to(x, y)
        if check_dirt(x, y):
            dirtFound = True
            break

    if dirtFound:
        break

    # move down to next row
    if y == MaxY:
        break
    y += 1
    move_to(x, y)
    if check_dirt(x, y):
        dirtFound = True
        break

# Indicate dirt collected
if dirtFound:
    # "clean" animation: flash the dirt cell a couple times
    flash = turtle.Turtle(visible=False)
    flash.speed(0)
    for _ in range(2):
        stamp_cell(flash, dirtX, dirtY, "gold")
        screen.update()
        time.sleep(0.2)
        stamp_cell(flash, dirtX, dirtY, "white")  # wipe
        stamp_cell(flash, dirtX, dirtY, "sienna") # redraw dirt (briefly)
        screen.update()
        time.sleep(0.2)
    # finally wipe dirt cell (collected)
    stamp_cell(flash, dirtX, dirtY, "white")
    screen.update()

# Return to dock (Manhattan path)
while x != dockX:
    x += -1 if x > dockX else 1
    move_to(x, y)

while y != dockY:
    y += -1 if y > dockY else 1
    move_to(x, y)

# Final message
msg = turtle.Turtle(visible=False)
msg.up()
msg.goto(0, -GRID_H/2 - 25)
msg.write("RETURNED HOME ✅", align="center", font=("Arial", 16, "bold"))
screen.update()

# Keep window open
turtle.done()