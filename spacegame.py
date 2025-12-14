
import pgzrun
import random
#Screen Setup
WIDTH, HEIGHT = 800, 600
TITLE = "Spaceship & Stars"

NUM_STARS = 8
NUM_SATELLITES = 4
SHIP_SPEED = 5
SAT_MIN_SPEED, SAT_MAX_SPEED = 2, 4
MARGIN = 30
HIT_COOLDOWN_S = 0.4
GAME_DURATION = 30  # seconds

score = 0
time_left = GAME_DURATION
game_over = False
damage_lock = False

spaceship = Actor("spaceship")
stars = []
satellites = []
#defining
def random_pos():
    return (random.randint(MARGIN, WIDTH - MARGIN),
            random.randint(MARGIN, HEIGHT - MARGIN))

def nonzero_speed():
    vx = random.choice([-1, 1]) * random.randint(SAT_MIN_SPEED, SAT_MAX_SPEED)
    vy = random.choice([-1, 1]) * random.randint(SAT_MIN_SPEED, SAT_MAX_SPEED)
    return vx, vy

def spawn_stars():
    global stars
    stars = [Actor("star", pos=random_pos()) for _ in range(NUM_STARS)]

def spawn_satellites():
    global satellites
    satellites = []
    for _ in range(NUM_SATELLITES):
        sat = Actor("satellite", pos=random_pos())
        sat.vx, sat.vy = nonzero_speed()
        satellites.append(sat)

def reset_star(star):
    star.pos = random_pos()
    if spaceship.colliderect(star):
        star.pos = random_pos()

def bounce_satellite(sat):
    sat.x += sat.vx
    sat.y += sat.vy
    if sat.left < 0:
        sat.left = 0; sat.vx *= -1
    elif sat.right > WIDTH:
        sat.right = WIDTH; sat.vx *= -1
    if sat.top < 0:
        sat.top = 0; sat.vy *= -1
    elif sat.bottom > HEIGHT:
        sat.bottom = HEIGHT; sat.vy *= -1

def handle_input():
    if keyboard.RIGHT and spaceship.right < WIDTH: spaceship.x += SHIP_SPEED
    if keyboard.LEFT and spaceship.left > 0:spaceship.x -= SHIP_SPEED
    if keyboard.UP and spaceship.top > 0: spaceship.y -= SHIP_SPEED
    if keyboard.DOWN and spaceship.bottom < HEIGHT:spaceship.y += SHIP_SPEED

def reset_damage_lock():
    global damage_lock
    damage_lock = False

def check_collisions():
    global score, damage_lock
    for s in stars:
        if spaceship.colliderect(s):
            score += 5
            reset_star(s)
    for sat in satellites:
        if spaceship.colliderect(sat) and not damage_lock:
            score -= 5
            damage_lock = True
            clock.schedule(reset_damage_lock, HIT_COOLDOWN_S)

def tick_time():
    global time_left, game_over
    if game_over: return
    time_left -= 1
    if time_left <= 0:
        game_over = True

def init_game():
    global score, time_left, game_over, damage_lock
    score = 0
    time_left = GAME_DURATION
    game_over = False
    damage_lock = False
    spaceship.pos = (WIDTH // 2, HEIGHT // 2)
    spawn_stars()
    spawn_satellites()
    clock.unschedule(tick_time)
    clock.schedule_interval(tick_time, 1)

def draw():
    screen.fill("black")
    if not game_over:
        for s in stars: s.draw()
        for sat in satellites: sat.draw()
        spaceship.draw()
        screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=36, color="white")
        screen.draw.text(f"Time: {time_left}s", topleft=(10, 50), fontsize=28, color="gray")
        screen.draw.text("Arrow keys to move | R to restart", topleft=(10, 85), fontsize=22, color="gray")
    else:
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2 - 20), fontsize=64, color="white")
        screen.draw.text(f"Final Score: {score}", center=(WIDTH/2, HEIGHT/2 + 40), fontsize=40, color="gray")
        screen.draw.text("Press R to restart", center=(WIDTH/2, HEIGHT/2 + 90), fontsize=28, color="gray")

def update():
    if game_over: return
    handle_input()
    for sat in satellites:
        bounce_satellite(sat)
    check_collisions()

def on_key_down(key):
       if key == keys.R:
        init_game()

init_game()

pgzrun.go()

