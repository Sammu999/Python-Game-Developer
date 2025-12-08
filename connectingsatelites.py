import pgzrun
import random

WIDTH=600
HEIGHT=500
TITLE="Connecting Satellites"

#Game Variables
satellites=[]
num_satellites=10

#Satellites
for i in range(num_satellites):
    satellite=Actor ("satellite")
    satellite.pos = random.randint (50,WIDTH-50),random.randint (50,HEIGHT-50)
    satellites.append(satellite)

def draw():
    screen.blit ("space_background",(0,0))
    n=1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(n),(satellite.x,satellite.y),fontsize=50,color="blue")
        n+=1
        


pgzrun.go()

