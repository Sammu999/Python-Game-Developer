import pgzrun
import random

WIDTH = 400
HEIGHT = 400

def draw():
    screen.fill("black")
    size = 380
    
    for i in range(12):
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
        # Rectangle layer
        rect = Rect((WIDTH/2 - size/2, HEIGHT/2 - size/2), (size, size))
        if i % 2 == 0:
            screen.draw.rect(rect, color)
        else:
            screen.draw.filled_rect(rect, color)
        
        # Circle layer
        if i % 2 == 0:
            screen.draw.circle((WIDTH/2, HEIGHT/2), size/2, color)
        else:
            screen.draw.filled_circle((WIDTH/2, HEIGHT/2), size/2, color)
        
        # Line layer (cross lines through center)
        screen.draw.line((WIDTH/2 - size/2, HEIGHT/2), (WIDTH/2 + size/2, HEIGHT/2), color)
        screen.draw.line((WIDTH/2, HEIGHT/2 - size/2), (WIDTH/2, HEIGHT/2 + size/2), color)
        
        size = size-30

pgzrun.go()

