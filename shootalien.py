import pgzrun
import random
WIDTH=400
HEIGHT=400
TITLE="Shooting Alien Game"
alien = Actor ("alien")
alien.pos=100,150
message=""
def draw():
    screen.fill("red")
    alien.draw()
    screen.draw.text("Alien Shooting game",center=(200,50),fontsize=25,color="blue")
    screen.draw.text(message,center=(200,100),fontsize=25,color="blue")
    
def on_mouse_down(pos):
    global message
    print(pos)
    if alien.collidepoint(pos):
        message="You hit the alien!"
        alien.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
    else:
        message="Oops you missed it!"

pgzrun.go()