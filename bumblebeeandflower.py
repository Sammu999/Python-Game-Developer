import pgzrun
import random
WIDTH=600
HEIGHT=500
TITLE="Bumblebbe and flower game"
bee=Actor ("bee")
flower=Actor ("flower")
bee.pos=random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50) 
flower.pos=random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50) 
score = 0
game_over=False

def draw():
    if not game_over:
        screen.blit("background",(0,0))
        bee.draw()
        flower.draw()
        screen.draw.text("Score =" + str(score),(10,10)) 
    else:
        screen.fill("blue")
        screen.draw.text("Game Over. Your final score is" + str(score),center=(WIDTH/2,HEIGHT/2)) 
    

# def on_key_down(key):
#     if key == keys.RIGHT:
#         bee.x = bee.x + 5
# Doesn't work for continuous pressing. Only works for separate clicking on key.

def update():
    global score
    if keyboard.RIGHT and bee.right < WIDTH:
        bee.x = bee.x + 5
    elif keyboard.LEFT and bee.left > 0:
        bee.x = bee.x - 5
    if keyboard.UP and bee.top > 0:
        bee.y = bee.y - 5
    elif keyboard.DOWN and bee.bottom < HEIGHT:
        bee.y = bee.y + 5
    
    if bee.colliderect(flower):
        flower.pos=random.randint(0,WIDTH-50),random.randint(0,HEIGHT-50)
        score = score + 5

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up,10)

         



    
    

pgzrun.go()


