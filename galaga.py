import pgzrun
WIDTH = 800
HEIGHT = 800
game_state = "launch"

galaga = Actor ("galaga")
galaga.pos = (WIDTH/2, HEIGHT-50)

enemies = []
ypos = 50
for i in range (4):
    enemy_row = []
    xpos = 50
    
    for a in range (5):
        enemy = Actor ("enemy")
        enemy.x = xpos
        enemy.y = ypos
        
        enemy_row.append (enemy)
        xpos += 75

    ypos += 50

    enemies.append (enemy_row)

direction = 1


def draw():
    screen.fill ("cyan")
    if game_state == "launch":
        screen.draw.text("Welcome to the Galaga Game",center = (WIDTH/2,HEIGHT/2), color="black", fontsize=50)
        screen.draw.text("Press any key to continue",center = (WIDTH/2 , HEIGHT/2+50), color = "black" , fontsize = 25)
    
    elif game_state == "start":
        galaga.draw()
        for enemy_row in enemies:
            for enemy in enemy_row:
                enemy.draw()
            

       

    


def update():
    global direction
    if keyboard.A and galaga.x >= 0:
        galaga.x -= 10

    if keyboard.D and galaga.x <= WIDTH:
        galaga.x += 10
    
    if enemies [0] [-1].x >= WIDTH or enemies [0] [0].x <= 0:
        direction*=-1
    for  enemy_row in enemies:
        for enemy in enemy_row:
            enemy.x += 2*direction




def on_key_down(key):
    global game_state

    if game_state == "launch":
        game_state = "start"

    



pgzrun.go()
    




