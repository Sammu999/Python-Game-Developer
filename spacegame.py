import pgzrun
import random
import pygame
from pgzero.loaders import images

WIDTH = 600
HEIGHT = 500
TITLE = "Space Explorer"

ship = Actor("ship")
star = Actor("star")
asteroid = Actor("asteroid")

ship._surf = pygame.transform.smoothscale(images.load("ship"), (60, 60))
star._surf = pygame.transform.smoothscale(images.load("star"), (30, 30))
asteroid._surf = pygame.transform.smoothscale(images.load("asteroid"), (70, 70))

background = pygame.transform.smoothscale(images.load("space"), (WIDTH, HEIGHT))

ship.pos = (WIDTH // 2, HEIGHT // 2)
star.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
asteroid.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

score = 0
game_over = False

def draw():
    if not game_over:
        screen.blit(background, (0, 0))
        ship.draw()
        star.draw()
        asteroid.draw()
        screen.draw.text("Score: " + str(score), (10, 10), color="white")
    else:
        screen.fill("black")
        screen.draw.text("Game Over! Final Score: " + str(score),
                         center=(WIDTH/2, HEIGHT/2), fontsize=40, color="yellow")

def update():
    global score
    if keyboard.RIGHT and ship.right < WIDTH:
        ship.x = ship.x + 5
    if keyboard.LEFT and ship.left > 0:
        ship.x = ship.x - 5
    if keyboard.UP and ship.top > 0:
        ship.y = ship.y - 5
    if keyboard.DOWN and ship.bottom < HEIGHT:
        ship.y = ship.y + 5

    if ship.colliderect(star):
        score = score + 10
        star.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    if ship.colliderect(asteroid):
        score = score - 5
        asteroid.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    asteroid.x = asteroid.x + random.randint(-1, 1)
    asteroid.y = asteroid.y + random.randint(-1, 1)

    if asteroid.left < 0:
        asteroid.left = 0
    if asteroid.right > WIDTH:
        asteroid.right = WIDTH
    if asteroid.top < 0:
        asteroid.top = 0
    if asteroid.bottom > HEIGHT:
        asteroid.bottom = HEIGHT

def on_mouse_down(pos):
    global score
    if star.collidepoint(pos):
        score = score + 15
        star.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 40)

pgzrun.go()
