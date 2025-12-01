import pgzrun
import random

WIDTH=400
HEIGHT=400
TITLE="Treasure Hunt Game"

treasure=Actor("bee")
treasure.scale=0.2 
treasure.pos=200, 200

message=""

def draw():
    screen.fill("gold")
    treasure.draw()
    screen.draw.text("Treasure Hunt!", center=(200, 50), fontsize=30, color="red")
    screen.draw.text(message, center=(200, 100), fontsize=25, color="black")

def on_mouse_down(pos):
    global message
    if treasure.collidepoint(pos):
        message="You found the treasure!"
        treasure.pos=random.randint(50 ,WIDTH - 50), random.randint( 50,HEIGHT - 50)
    else:
        message="Empty spot... keep searching!"

pgzrun.go()