import pgzrun
import random

WIDTH = 600
HEIGHT = 500
TITLE = "Connecting Satellites"

# Game Variables
satellites = []
num_satellites = 10
current_satellite = 0
lines = []

# Timer
timer = 0
timer_running = True

# Create Satellites
for i in range(num_satellites):
    satellite = Actor("satellite")
    satellite.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    satellites.append(satellite)

def update():
    global timer
    if timer_running:
        timer += 1/60   

def draw():
    screen.blit("space_background", (0, 0))
    

    
    n = 1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(n), (satellite.x - 20, satellite.y - 50),
                         fontsize=40, color="blue")
        n += 1

    # Draw connecting lines
    for line in lines:
        screen.draw.line(line[0], line[1], "red")

    
    screen.draw.text(str(int(timer)) + "s",
                     (WIDTH - 120, 10),
                     fontsize=40,
                     color="white")

   
    if current_satellite == num_satellites:
        screen.draw.text("Mission Complete!",
                         (150, 20),
                         fontsize=60,
                         color="yellow")

def on_mouse_down(pos):
    global current_satellite, lines, timer_running, timer

    if current_satellite < num_satellites:
        if satellites[current_satellite].collidepoint(pos):

           
            if current_satellite > 0:
                lines.append([
                    satellites[current_satellite - 1].pos,
                    satellites[current_satellite].pos
                ])

            current_satellite += 1

            # Stop timer when finished
            if current_satellite == num_satellites:
                timer_running = False

        else:
           
            current_satellite = 0
            lines = []
            timer = 0
            timer_running = True

pgzrun.go()