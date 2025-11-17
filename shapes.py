import pgzrun
import random
WIDTH=400
HEIGHT=400
def draw():
    screen.fill("black")
    size=400
   
    for i in range(25):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)


        rec=Rect(0,0,size,size)
        rec.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(rec,(r,g,b))
        size=size-20


pgzrun.go()