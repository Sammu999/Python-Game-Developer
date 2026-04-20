import pgzrun

WIDTH = 800
HEIGHT = 800

game_state = "launch"
score = 0
end_message = ""

galaga = Actor("galaga")
galaga.pos = (WIDTH/2, HEIGHT - 50)


enemies = []
ypos = 50
for i in range(4):
    enemy_row = []
    xpos = 50

    for a in range(5):
        enemy = Actor("enemy")
        enemy.x = xpos
        enemy.y = ypos

        enemy_row.append(enemy)
        xpos += 75

    ypos += 50
    enemies.append(enemy_row)

direction = 1
bullets = []

def shoot():
    
    bullet = Rect((galaga.x - 2, galaga.y - 20), (5, 15))
    bullets.append(bullet)

def draw():
    screen.fill("cyan")

    if game_state == "launch":
        screen.draw.text("Welcome to the Galaga Game",
                         center=(WIDTH/2, HEIGHT/2),
                         color="black", fontsize=50)
        screen.draw.text("Press any key to continue",
                         center=(WIDTH/2, HEIGHT/2 + 50),
                         color="black", fontsize=25)

    elif game_state == "start":
        galaga.draw()


        for enemy_row in enemies:
            for enemy in enemy_row:
                enemy.draw()

        
        for bullet in bullets:
            screen.draw.filled_rect(bullet, "white")
  
        screen.draw.text(f"Score: {score}", (5,5), color = "black")

    elif game_state == "over":
        screen.fill ("red")
        screen.draw.text(end_message, fontsize = 45,center =(WIDTH/2,HEIGHT/2), color = "black")
        screen.draw.text(f"You have scored {score}",fontsize = 45, center = (WIDTH/2, HEIGHT/2 + 30), color = "black")

def update():
    global direction, score, end_message, game_state
    move_down = False
    if keyboard.A and galaga.x >= 0:
        galaga.x -= 10
    if keyboard.D and galaga.x <= WIDTH:
        galaga.x += 10

    if any (enemies):
        if enemies[0][-1].x >= WIDTH or enemies[0][0].x <= 0:
            direction *= -1
            move_down = True
    else: 
        end_message = "You have lost to the enemies!"
        game_state = "over"



       
    for enemy_row in enemies:
        for enemy in enemy_row:
            enemy.x += 3 * direction
            if move_down:
                enemy.y += 40

    for bullet in bullets:
        bullet.y -= 10
   
    for bullet in bullets[:]:
        if bullet.y < 0:
            bullets.remove(bullet)

    for i in range(len(enemies)):
        for enemy in enemies[i]:
            for bullet in bullets:
            
                if enemy.colliderect(bullet):
                    bullets.remove(bullet)
                    enemies[i].remove(enemy)
                    score += 1
                    print (enemies)
   # if len (enemies) == 0 :
    
    for enemy_row in enemies:
        for enemy in enemy_row:
            if enemy.colliderect(galaga):
                end_message = "You have lost to the enemies!"
                game_state = "over"
        





                    

def on_key_down(key):
    global game_state

    if game_state == "launch":
        game_state = "start"

    elif game_state == "start":
        if key == keys.SPACE:
            shoot()

pgzrun.go()